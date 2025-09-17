document.addEventListener("DOMContentLoaded", () => {
  chrome.storage.local.get(["summary", "risks", "rewrite"], (data) => {
    document.getElementById("summary").textContent = data.summary || "No result";
    document.getElementById("risks").textContent = data.risks || "No result";
    document.getElementById("rewrite").textContent = data.rewrite || "No result";
  });
});