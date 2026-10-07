> For the complete documentation index, see [llms.txt](https://support.backpack.exchange/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://support.backpack.exchange/legal/vara-disclosures/price-quotes.md).

# Price Quotes

For spot trading, the price of each Virtual Asset is solely determined by users on the orderbook (i.e., the price other users are willing to buy or sell).

Such market price may be influenced by a number of factors, such as liquidity of the token and market volatility.

For the convert feature, Backpack Exchange operates a request-for-quote system whereby (1) a user will submit a request to purchase or sell a given number of Virtual Assets, (2) Backpack Exchange will request quotes from liquidity providers to fulfill the users' request, and (3) provide the user with the best quote with a small additional spread charged by Backpack Exchange.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the following URL with the `ask` and `goal` query parameters:

```
GET https://support.backpack.exchange/legal/vara-disclosures/price-quotes.md?ask=<question>&goal=<user_goal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is what the user is ultimately trying to achieve, the reason they need the answer. Sharing it helps GitBook give you a better, more relevant answer. A goal is most helpful when it describes the outcome the user wants rather than restating the question. For example, with `ask=how do I create an API token`, a goal like `build a script that syncs our docs to a CMS` lets GitBook tailor the answer to that use case.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
