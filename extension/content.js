// Listen for messages from background.js
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "showPanel") {
    createSidebar(message.simplifiedText);
  }
});

function createSidebar(text) {
  // If sidebar already exists, update it
  let existing = document.getElementById("ai-simplify-sidebar");
  if (existing) {
    existing.querySelector(".ai-simplify-content").innerText = text;
    existing.style.display = "block";
    return;
  }

  // Sidebar container
  const sidebar = document.createElement("div");
  sidebar.id = "ai-simplify-sidebar";
  sidebar.style.position = "fixed";
  sidebar.style.top = "0";
  sidebar.style.right = "0";
  sidebar.style.width = "350px";
  sidebar.style.height = "100%";
  sidebar.style.background = "white";
  sidebar.style.borderLeft = "2px solid #ccc";
  sidebar.style.zIndex = "999999";  // ensure it's always on top
  sidebar.style.boxShadow = "-2px 0 5px rgba(0,0,0,0.2)";
  sidebar.style.fontFamily = "Arial, sans-serif";
  sidebar.style.display = "flex";
  sidebar.style.flexDirection = "column";

  // Header
  const header = document.createElement("div");
  header.innerText = "Simplified Text";
  header.style.background = "#4285f4";
  header.style.color = "white";
  header.style.padding = "10px";
  header.style.fontWeight = "bold";
  header.style.display = "flex";
  header.style.justifyContent = "space-between";
  header.style.alignItems = "center";

  // Close button
  const closeBtn = document.createElement("span");
  closeBtn.innerText = "✖";
  closeBtn.style.cursor = "pointer";
  closeBtn.onclick = () => {
    sidebar.style.display = "none";
  };

  header.appendChild(closeBtn);

  // Content
  const content = document.createElement("div");
  content.className = "ai-simplify-content";
  content.innerText = text;
  content.style.padding = "15px";
  content.style.overflowY = "auto";
  content.style.flex = "1";

  sidebar.appendChild(header);
  sidebar.appendChild(content);
  document.body.appendChild(sidebar);
}
