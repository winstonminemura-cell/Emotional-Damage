# Morrow local AI setup

This website runs the Llama 3.1 8B model through Ollama on this computer. Messages sent from the website go to the local Ollama service; the site does not use a hosted AI API. Approved preferences in the browser are included as conversation context. This is personalization through prompts and saved notes, not fine-tuning or changing model weights.

## One-time setup

1. Install Ollama for Windows from https://ollama.com/download/windows if it is not already installed.
2. Open PowerShell in this folder and run:

   ```powershell
   ollama pull llama3.1:8b
   ```

   The quantized model download is about 4.9 GB.
3. Start the site with:

   ```powershell
   .\run_local.ps1
   ```

   Keep the PowerShell window open. The page opens at http://127.0.0.1:8000.

## Privacy controls

Chats and approved memories remain in this browser's local storage. The text of each message is sent to Ollama on this same computer to produce a reply. Use the private chat control to avoid saving conversation history. Clear browser memories with “Start fresh.”
