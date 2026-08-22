(function () {
    function injectStyles() {
        const css = [
            ".live-demo{margin:1.25rem 0;border:0.5px solid var(--border, #d8d6cd);border-radius:8px;overflow:hidden;}",
            ".live-demo-bar{display:flex;justify-content:space-between;align-items:center;padding:6px 12px;background:var(--surface-1, #f1efe8);font-size:13px;}",
            ".live-demo-bar button{font-size:12px;padding:3px 10px;border:0.5px solid var(--border-strong, #b4b2a9);border-radius:6px;background:#fff;cursor:pointer;}",
            ".live-demo-bar button:hover{background:var(--surface-1, #f1efe8);}",
            ".live-demo-panes{display:grid;grid-template-columns:1fr 1fr;}",
            "@media (max-width:640px){.live-demo-panes{grid-template-columns:1fr;}}",
            ".live-demo-code-col{display:flex;flex-direction:column;border-right:0.5px solid var(--border, #d8d6cd);}",
            ".live-demo-code-col label{font-size:11px;text-transform:uppercase;letter-spacing:0.03em;color:var(--text-soft, #7a7869);padding:4px 10px 0;}",
            ".live-demo textarea{width:100%;min-height:110px;border:none;border-top:0.5px solid var(--border, #d8d6cd);padding:8px 10px;font-family:monospace;font-size:13px;resize:vertical;box-sizing:border-box;}",
            ".live-demo-code-col label:first-child + textarea{border-top:none;}",
            ".live-demo iframe{width:100%;min-height:220px;border:none;background:#fff;resize:vertical;overflow:auto;display:block;}",
            ".live-demo-single textarea{min-height:160px;resize:vertical;}"
        ].join("");
        const style = document.createElement("style");
        style.textContent = css;
        document.head.appendChild(style);
    }

    function makeBar(label) {
        const bar = document.createElement("div");
        bar.className = "live-demo-bar";
        bar.innerHTML = "<span>" + (label || "✏️ Probeer het zelf") + "</span>";
        const resetBtn = document.createElement("button");
        resetBtn.type = "button";
        resetBtn.textContent = "Reset";
        bar.appendChild(resetBtn);
        return { bar: bar, resetBtn: resetBtn };
    }

    function makeTextarea(labelText, value) {
        const label = document.createElement("label");
        label.textContent = labelText;
        const textarea = document.createElement("textarea");
        textarea.spellcheck = false;
        textarea.value = value;
        return { label: label, textarea: textarea };
    }

    // Single HTML-only widget
    function buildHtmlOnlyWidget(originalCode) {
        const wrap = document.createElement("div");
        wrap.className = "live-demo";
        const barParts = makeBar();
        wrap.appendChild(barParts.bar);

        const panes = document.createElement("div");
        panes.className = "live-demo-panes";
        const ta = makeTextarea("HTML", originalCode);
        panes.appendChild(ta.textarea);

        const iframe = document.createElement("iframe");
        iframe.setAttribute("sandbox", "allow-same-origin");
        panes.appendChild(iframe);
        wrap.appendChild(panes);

        function render() { iframe.srcdoc = ta.textarea.value; }
        let timer = null;
        ta.textarea.addEventListener("input", function () {
            clearTimeout(timer);
            timer = setTimeout(render, 300);
        });
        barParts.resetBtn.addEventListener("click", function () {
            ta.textarea.value = originalCode;
            render();
        });
        render();
        return wrap;
    }

    // Combined HTML + CSS widget (static styling, no scripts)
    function buildHtmlCssWidget(originalHtml, originalCss) {
        const wrap = document.createElement("div");
        wrap.className = "live-demo";
        const barParts = makeBar();
        wrap.appendChild(barParts.bar);

        const panes = document.createElement("div");
        panes.className = "live-demo-panes";
        const codeCol = document.createElement("div");
        codeCol.className = "live-demo-code-col";
        const htmlTa = makeTextarea("HTML", originalHtml);
        const cssTa = makeTextarea("CSS", originalCss);
        codeCol.appendChild(htmlTa.label);
        codeCol.appendChild(htmlTa.textarea);
        codeCol.appendChild(cssTa.label);
        codeCol.appendChild(cssTa.textarea);

        const iframe = document.createElement("iframe");
        iframe.setAttribute("sandbox", "allow-same-origin");
        panes.appendChild(codeCol);
        panes.appendChild(iframe);
        wrap.appendChild(panes);

        function render() {
            iframe.srcdoc = "<style>" + cssTa.textarea.value + "</style>" + htmlTa.textarea.value;
        }
        let timer = null;
        function scheduleRender() {
            clearTimeout(timer);
            timer = setTimeout(render, 300);
        }
        htmlTa.textarea.addEventListener("input", scheduleRender);
        cssTa.textarea.addEventListener("input", scheduleRender);
        barParts.resetBtn.addEventListener("click", function () {
            htmlTa.textarea.value = originalHtml;
            cssTa.textarea.value = originalCss;
            render();
        });
        render();
        return wrap;
    }

    // Combined HTML + JS widget: the JS actually runs against the HTML in the
    // iframe (DOM manipulation, event listeners are clickable and live).
    // sandbox="allow-scripts" only — isolated opaque origin, no access to the
    // parent page. fetch() to external APIs still works from here.
    function buildHtmlJsWidget(originalHtml, originalJs) {
        const wrap = document.createElement("div");
        wrap.className = "live-demo";
        const barParts = makeBar("▶️ Probeer het zelf — klik en typ in de preview");
        wrap.appendChild(barParts.bar);

        const panes = document.createElement("div");
        panes.className = "live-demo-panes";
        const codeCol = document.createElement("div");
        codeCol.className = "live-demo-code-col";
        const htmlTa = makeTextarea("HTML", originalHtml);
        const jsTa = makeTextarea("JavaScript", originalJs);
        codeCol.appendChild(htmlTa.label);
        codeCol.appendChild(htmlTa.textarea);
        codeCol.appendChild(jsTa.label);
        codeCol.appendChild(jsTa.textarea);

        const iframe = document.createElement("iframe");
        iframe.setAttribute("sandbox", "allow-scripts");
        panes.appendChild(codeCol);
        panes.appendChild(iframe);
        wrap.appendChild(panes);

        function render() {
            iframe.srcdoc =
                htmlTa.textarea.value +
                "<script>try{" + jsTa.textarea.value + "}catch(e){document.body.insertAdjacentHTML('beforeend','<p style=\"color:#e06c75;font-family:monospace;\">Fout: '+e.message+'</p>');}<\/script>";
        }
        let timer = null;
        function scheduleRender() {
            clearTimeout(timer);
            timer = setTimeout(render, 400);
        }
        htmlTa.textarea.addEventListener("input", scheduleRender);
        jsTa.textarea.addEventListener("input", scheduleRender);
        barParts.resetBtn.addEventListener("click", function () {
            htmlTa.textarea.value = originalHtml;
            jsTa.textarea.value = originalJs;
            render();
        });
        render();
        return wrap;
    }

    // JavaScript-only widget: one textarea + a simulated console output pane.
    // sandbox="allow-scripts" (no allow-same-origin) — isolated opaque origin.
    function buildJsConsoleWidget(originalCode) {
        const wrap = document.createElement("div");
        wrap.className = "live-demo";
        const barParts = makeBar("▶️ Probeer het zelf — bekijk de console-uitvoer");
        wrap.appendChild(barParts.bar);

        const panes = document.createElement("div");
        panes.className = "live-demo-panes";
        const ta = makeTextarea("JavaScript", originalCode);
        panes.appendChild(ta.textarea);

        const iframe = document.createElement("iframe");
        iframe.setAttribute("sandbox", "allow-scripts");
        panes.appendChild(iframe);
        wrap.appendChild(panes);

        function consoleHarness(userCode) {
            return (
                "<style>" +
                "body{font-family:monospace;font-size:13px;padding:10px;background:#1e1e1e;color:#d4d4d4;margin:0;}" +
                ".line{white-space:pre-wrap;word-break:break-word;padding:2px 0;border-bottom:1px solid #2a2a2a;}" +
                ".log{color:#d4d4d4;} .warn{color:#e5c07b;} .error{color:#e06c75;}" +
                "</style><div id='output'></div><script>" +
                "const out = document.getElementById('output');" +
                "function fmt(a){try{return typeof a==='object'&&a!==null?JSON.stringify(a):String(a);}catch(e){return String(a);}}" +
                "function print(cls, args){const d=document.createElement('div');d.className='line '+cls;" +
                "d.textContent=Array.prototype.map.call(args, fmt).join(' ');out.appendChild(d);}" +
                "console.log=function(){print('log', arguments);};" +
                "console.info=function(){print('log', arguments);};" +
                "console.debug=function(){print('log', arguments);};" +
                "console.warn=function(){print('warn', arguments);};" +
                "console.error=function(){print('error', arguments);};" +
                "console.table=function(){print('log', arguments);};" +
                "console.dir=function(){print('log', arguments);};" +
                "try{" + userCode + "}catch(e){print('error', ['Fout: ' + e.message]);}" +
                "</script>"
            );
        }

        function render() { iframe.srcdoc = consoleHarness(ta.textarea.value); }
        let timer = null;
        ta.textarea.addEventListener("input", function () {
            clearTimeout(timer);
            timer = setTimeout(render, 400);
        });
        barParts.resetBtn.addEventListener("click", function () {
            ta.textarea.value = originalCode;
            render();
        });
        render();
        return wrap;
    }

    function detectLanguage(codeEl) {
        const m = /language-(\w+)/.exec(codeEl.className || "");
        if (!m) return null;
        if (m[1] === "javascript") return "js";
        return m[1];
    }

    function init() {
        injectStyles();

        const lessonContent = document.querySelector(".lesson-content");
        if (!lessonContent) return;

        const blocks = [];
        lessonContent.querySelectorAll("pre > code").forEach(function (code) {
            const lang = detectLanguage(code);
            if (lang === "html" || lang === "css" || lang === "js") {
                blocks.push({ pre: code.parentElement, lang: lang, code: code.textContent });
            }
        });

        let i = 0;
        while (i < blocks.length) {
            const current = blocks[i];
            const next = blocks[i + 1];

            if (next && current.lang === "html" && next.lang === "js") {
                current.pre.replaceWith(buildHtmlJsWidget(current.code, next.code));
                next.pre.remove();
                i += 2;
                continue;
            }

            if (next && current.lang === "js" && next.lang === "html") {
                current.pre.replaceWith(buildHtmlJsWidget(next.code, current.code));
                next.pre.remove();
                i += 2;
                continue;
            }

            if (next && current.lang === "css" && next.lang === "html") {
                current.pre.replaceWith(buildHtmlCssWidget(next.code, current.code));
                next.pre.remove();
                i += 2;
                continue;
            }

            if (next && current.lang === "html" && next.lang === "css") {
                current.pre.replaceWith(buildHtmlCssWidget(current.code, next.code));
                next.pre.remove();
                i += 2;
                continue;
            }

            if (current.lang === "html") {
                current.pre.replaceWith(buildHtmlOnlyWidget(current.code));
                i += 1;
                continue;
            }

            if (current.lang === "js") {
                current.pre.replaceWith(buildJsConsoleWidget(current.code));
                i += 1;
                continue;
            }

            // Lone CSS block: nothing to render it against — left as plain code.
            i += 1;
        }
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", init);
    } else {
        init();
    }
})();
