const editor = CodeMirror.fromTextArea(document.getElementById("editor"), {
    mode: "python",
    theme: "default",
    lineNumbers: true,
    indentUnit: 4,
    smartIndent: true
  });
  
  // Detect space key
  editor.on("keydown", async function (cm, event) {
    if (event.key === " ") {
      const code = cm.getValue();
      try {
        const response = await fetch("http://127.0.0.1:5000/suggest", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ code })
        });
  
        const data = await response.json();
        if (data && data.suggestion) {
          cm.replaceRange("\n" + data.suggestion, cm.getCursor());
        }
      } catch (err) {
        console.error("Error getting suggestion:", err);
      }
    }
  });
  