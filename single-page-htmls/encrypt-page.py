#!/usr/bin/env python3
"""Encrypt an HTML file with AES-256-GCM for static-site password protection.

Usage: python3 encrypt-page.py <input.html> <password> [output.html]

Uses Node.js crypto module for AES-256-GCM (available on any system with Node).
"""

import base64
import json
import os
import subprocess
import sys
import tempfile


SHELL_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Protected Page</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    background: #0d1117; color: #e6edf3;
    display: flex; align-items: center; justify-content: center;
    min-height: 100vh;
  }
  .lock-box {
    background: #161b22; border: 1px solid #30363d; border-radius: 12px;
    padding: 40px 36px; max-width: 380px; width: 90%; text-align: center;
    box-shadow: 0 4px 24px rgba(0,0,0,0.4);
  }
  .lock-box h1 { font-size: 20px; margin-bottom: 8px; }
  .lock-box p { font-size: 14px; color: #9198a1; margin-bottom: 24px; }
  .lock-box input {
    width: 100%; padding: 10px 14px; font-size: 15px;
    background: #0d1117; color: #e6edf3; border: 1px solid #30363d;
    border-radius: 8px; margin-bottom: 14px; outline: none;
  }
  .lock-box input:focus { border-color: #4493f8; }
  .lock-box button {
    width: 100%; padding: 10px; font-size: 15px; font-weight: 600;
    background: #238636; color: #fff; border: none; border-radius: 8px;
    cursor: pointer;
  }
  .lock-box button:hover { background: #2ea043; }
  .lock-box .error { color: #f85149; font-size: 13px; margin-top: 10px; display: none; }
  .lock-icon { font-size: 36px; margin-bottom: 16px; }
</style>
</head>
<body>

<div class="lock-box" id="lockBox">
  <div class="lock-icon">&#x1F512;</div>
  <h1>Password Required</h1>
  <p>This page is encrypted. Enter the password to view it.</p>
  <form id="unlockForm">
    <input type="password" id="pwd" placeholder="Password" autofocus autocomplete="off">
    <button type="submit">Unlock</button>
  </form>
  <div class="error" id="err">Incorrect password. Please try again.</div>
</div>

<script>
(function() {
  var E = %%ENCRYPTED_DATA%%;

  function b64decode(s) {
    var bin = atob(s), arr = new Uint8Array(bin.length);
    for (var i = 0; i < bin.length; i++) arr[i] = bin.charCodeAt(i);
    return arr;
  }

  async function decrypt(password) {
    var enc = new TextEncoder();
    var keyMaterial = await crypto.subtle.importKey(
      'raw', enc.encode(password), 'PBKDF2', false, ['deriveKey']
    );
    var key = await crypto.subtle.deriveKey(
      { name: 'PBKDF2', salt: b64decode(E.salt), iterations: E.iter, hash: 'SHA-256' },
      keyMaterial,
      { name: 'AES-GCM', length: 256 },
      false,
      ['decrypt']
    );
    // Node crypto appends the 16-byte auth tag to ciphertext; Web Crypto expects the same
    var ct = b64decode(E.ct);
    var iv = b64decode(E.iv);
    var plain = await crypto.subtle.decrypt({ name: 'AES-GCM', iv: iv }, key, ct);
    return new TextDecoder().decode(plain);
  }

  document.getElementById('unlockForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    var pwd = document.getElementById('pwd').value;
    if (!pwd) return;
    try {
      var html = await decrypt(pwd);
      document.open();
      document.write(html);
      document.close();
    } catch (err) {
      document.getElementById('err').style.display = 'block';
      document.getElementById('pwd').value = '';
      document.getElementById('pwd').focus();
    }
  });
})();
</script>

</body>
</html>"""


NODE_ENCRYPT_SCRIPT = """
const crypto = require('crypto');
const fs = require('fs');

const inputPath = process.argv[2];
const password = process.argv[3];

const plaintext = fs.readFileSync(inputPath);
const salt = crypto.randomBytes(16);
const iv = crypto.randomBytes(12);
const iterations = 600000;

const key = crypto.pbkdf2Sync(password, salt, iterations, 32, 'sha256');
const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
const encrypted = Buffer.concat([cipher.update(plaintext), cipher.final()]);
const tag = cipher.getAuthTag();
// Web Crypto expects tag appended to ciphertext
const ct = Buffer.concat([encrypted, tag]);

const result = JSON.stringify({
  salt: salt.toString('base64'),
  iv: iv.toString('base64'),
  ct: ct.toString('base64'),
  iter: iterations
});

process.stdout.write(result);
"""


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <input.html> <password> [output.html]")
        sys.exit(1)

    input_path = sys.argv[1]
    password = sys.argv[2]
    output_path = sys.argv[3] if len(sys.argv) > 3 else input_path

    # Use Node.js for encryption (available everywhere, no pip deps)
    with tempfile.NamedTemporaryFile(mode='w', suffix='.js', delete=False) as f:
        f.write(NODE_ENCRYPT_SCRIPT)
        script_path = f.name

    try:
        result = subprocess.run(
            ['node', script_path, input_path, password],
            capture_output=True, text=True, check=True
        )
        encrypted_json = result.stdout
    finally:
        os.unlink(script_path)

    # Verify it's valid JSON
    encrypted = json.loads(encrypted_json)
    shell = SHELL_TEMPLATE.replace("%%ENCRYPTED_DATA%%", json.dumps(encrypted))

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(shell)

    plain_kb = os.path.getsize(input_path) / 1024
    out_kb = len(shell.encode()) / 1024
    print(f"Encrypted {plain_kb:.0f} KB -> {out_kb:.0f} KB ({output_path})")


if __name__ == "__main__":
    main()
