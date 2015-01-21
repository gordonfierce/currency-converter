# Currency converter

## Description

A set of functions to convert currency from one denomination to another.

To run, import currency and use the convert function with a list of conversion rates in the style:

```py
[("USD", "EUR", 0.86), ("USD", "BTC", 212.86)]
```

Pass currency.convert the rates list, an initial value, the first currency code, and the currency code of the currency to convert to.


## TODO

In addition to the requirements from **Normal Mode**:

* Make sure that if you try to make a conversion you do not know about, a `ValueError` is raised with an appropriate message.

* Test that you can convert between any two rates that you have the ability to, even if you do not have a direct conversion rate for them. For example, with the rates:

  ```py
  [("USD", "EUR", 0.74), ("EUR", "JPY", 145.949)]
  ```

  Make sure you can convert from USD to JPY.

  This will probably require [Dijkstra's algorithm](http://rosettacode.org/wiki/Dijkstra%27s_algorithm).


## Additional Resources

* [Currency charts](http://www.xe.com/currencycharts/) if you want accurate values.
* The [pytest](http://pytest.org/latest/) testing framework.
* [An Introduction to Test Driven Development](https://www.codeenigma.com/community/blog/introduction-test-driven-development).
* [Test-Driven Development](https://en.wikibooks.org/wiki/Introduction_to_Software_Engineering/Testing/Test-driven_Development) on Wikibooks.
* [Test-Driven Development by Example](http://www.amazon.com/Test-Driven-Development-By-Example/dp/0321146530), the canonical book on this stuff.
