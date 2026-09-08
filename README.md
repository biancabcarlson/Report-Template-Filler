# Report Template Filler

**🔗 Live demo:** https://biancabcarlson.github.io/Report-Template-Filler/

Every case report needs the same skeleton — case ID, account info, summary, findings, disposition — but retyping that structure each time (or copy-pasting from an old report and forgetting to update something) wastes time and invites mistakes.

Define your report template once — section headers and fields, fully customizable — then fill in a simple form and submit a consistently formatted report every time. No fields, categories, or report logic are prescribed by the tool; you control the entire structure. The demo's default template is prefilled from the `simulated-account` fixture (case info, account summary, Suspected Fraud Dates, findings, documents collected, a "Paste other tools output here" section, and a disposition marked "if confirmed fraud") and includes a **Transactions Captured** section, pulled from the same fixture, that you can edit in place and freely add or remove transactions from — the total recalculates live as you do, and removing one by mistake can be reversed with **Undo remove**. The Suspected Fraud Dates fields use a native date picker shown side by side in a fixed two-column layout (type or click to set), so neither box can grow into the other at narrow widths. Summary and Key Observations can be expanded to a larger textarea for easier editing and collapsed back down without losing anything typed. Documents Collected takes one document per line and renders as a bulleted list in the generated report (its section heading isn't repeated a second time as a field label).

**Paste other tools output here** holds one or more paste-in boxes for copied output from any of the other tools in this series (e.g. Timeline Builder's "Copy Timeline" or the Calculator's "Copy results") — pasted text is preserved as-is, monospaced, in both the preview and the generated report. Use **+ Add tool output** to paste in another block, the **✕** on a block to remove it, and **Undo remove** to bring back the last one removed.

Once everything looks right, **Submit Report** asks "Are you sure?" before finalizing — a single explicit confirm step (Cancel or go forward) rather than separate Generate/Copy buttons, so the report can't be finalized by an accidental click. Includes a browser-based live demo (`index.html`, linked above) that runs entirely client-side; nothing is saved, uploaded, or sent anywhere.

## Other tools in this series

- [Case Calculator](https://biancabcarlson.github.io/Case-Calculator/)
- [Report Template Filler](https://biancabcarlson.github.io/Report-Template-Filler/) *(this repo)*
- [OSINT Tool](https://biancabcarlson.github.io/OSINT-Tool/)
- [Case Doc Tracker](https://biancabcarlson.github.io/Case-Doc-Tracker/)
- [Entity Name Matcher](https://biancabcarlson.github.io/Entity-Name-Matcher/)
- [Case Timeline Builder](https://biancabcarlson.github.io/Case-Timeline-Builder/)
