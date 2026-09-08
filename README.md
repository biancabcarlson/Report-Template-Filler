# Report Template Filler

**🔗 Live demo:** https://biancabcarlson.github.io/Report-Template-Filler/

Every case report needs the same skeleton — case ID, account info, summary, findings, disposition — but retyping that structure each time (or copy-pasting from an old report and forgetting to update something) wastes time and invites mistakes.

Define your report template once — section headers and fields, fully customizable — then fill in a simple form and generate a consistently formatted report every time. No fields, categories, or report logic are prescribed by the tool; you control the entire structure. The demo's default template is prefilled from the `simulated-account` fixture (case info, account summary, Suspected Fraud Dates, findings, documents collected, an Attached Tool Output section, and a disposition marked "if confirmed fraud") and includes a **Transactions Captured** section, pulled from the same fixture, that you can edit in place and freely add or remove transactions from — the total recalculates live as you do. The Suspected Fraud Dates fields use a native date picker shown side by side (type or click to set), rather than two stacked full-width boxes. Summary and Key Observations can be expanded to a larger textarea for easier editing and collapsed back down without losing anything typed. Documents Collected takes one document per line and renders as a bulleted list in the generated report (its section heading isn't repeated a second time as a field label). Attached Tool Output is a paste-in box for copied output from any of the other tools in this series (e.g. Timeline Builder's "Copy Timeline" or the Calculator's "Copy results") — pasted text is preserved as-is, monospaced, in both the preview and the generated report. Includes a browser-based live demo (`index.html`, linked above) that runs entirely client-side; nothing is saved or uploaded.

## Other tools in this series

- [Case Calculator](https://biancabcarlson.github.io/Case-Calculator/)
- [Report Template Filler](https://biancabcarlson.github.io/Report-Template-Filler/) *(this repo)*
- [OSINT Tool](https://biancabcarlson.github.io/OSINT-Tool/)
- [Case Doc Tracker](https://biancabcarlson.github.io/Case-Doc-Tracker/)
- [Entity Name Matcher](https://biancabcarlson.github.io/Entity-Name-Matcher/)
- [Case Timeline Builder](https://biancabcarlson.github.io/Case-Timeline-Builder/)
