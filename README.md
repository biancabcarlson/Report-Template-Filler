# Report Template Filler

**🔗 Live demo:** https://biancabcarlson.github.io/Report-Template-Filler/

Every case report needs the same skeleton — case ID, account info, summary, findings, disposition — but retyping that structure each time (or copy-pasting from an old report and forgetting to update something) wastes time and invites mistakes.

Define your report template once — section headers and fields, fully customizable — then fill in a simple form and generate a consistently formatted report every time. No fields, categories, or report logic are prescribed by the tool; you control the entire structure. The demo's default template is prefilled from the `simulated-account` fixture (case info, account summary, Suspected Fraud Dates, findings, documents collected, and a disposition marked "if confirmed fraud") and includes an editable **Transactions Captured** section with a running total pulled from the same fixture — amounts, labels, and details can be corrected in place, and the total recalculates live. The Suspected Fraud Dates fields use a native date picker (type or click to set). Summary and Key Observations can be expanded to a larger textarea for easier editing and collapsed back down without losing anything typed. Documents Collected takes one document per line and renders as a bulleted list in the generated report. Includes a browser-based live demo (`index.html`, linked above) that runs entirely client-side; nothing is saved or uploaded.

## Other tools in this series

- [Case Calculator](https://biancabcarlson.github.io/Case-Calculator/)
- [Report Template Filler](https://biancabcarlson.github.io/Report-Template-Filler/) *(this repo)*
- [OSINT Tool](https://biancabcarlson.github.io/OSINT-Tool/)
- [Case Doc Tracker](https://biancabcarlson.github.io/Case-Doc-Tracker/)
- [Entity Name Matcher](https://biancabcarlson.github.io/Entity-Name-Matcher/)
- [Case Timeline Builder](https://biancabcarlson.github.io/Case-Timeline-Builder/)
