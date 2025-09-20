// Create context menu only once when the extension is installed
chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "simplifyText",
    title: "Simplify with AI",
    contexts: ["selection"]
  });
});

// Handle context menu click
chrome.contextMenus.onClicked.addListener(async (info, tab) => {
  if (info.menuItemId === "simplifyText" && info.selectionText) {
    try {
      // Call FastAPI backend
      const response = await fetch("https://demystifyinglegaldocuments.onrender.com/api/v1/simplify", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ selection: { text: info.selectionText } })
      });

      const data = await response.json();

      // Save all three results in storage
      chrome.storage.local.set({
        summary: data.summary || "No result",
        risks: data.risks || "No result",
        rewrite: data.rewrite || "No result"
      });

      // Open popup window to display the results
      chrome.windows.create({
        url: chrome.runtime.getURL("popup.html"),
        type: "popup",
        width: 400,
        height: 600
      });

    } catch (err) {
      console.error("Error calling backend:", err);
    }
  }
});

