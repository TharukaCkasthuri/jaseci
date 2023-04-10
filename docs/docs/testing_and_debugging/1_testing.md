# Unit testing in Jaseci

- [Unit testing in Jaseci](#unit-testing-in-jaseci)
  - [Creating test cases](#creating-test-cases)
  - [Runing test cases](#runing-test-cases)
  - [Using Yield](#using-yield)
  - [Using Global `root_node`](#using-global-root_node)

In unit testing, test cases are typically created by the developer or a dedicated testing team and executed automatically using specialized testing frameworks or tools. The tests are designed to be repeatable and should cover various scenarios, including normal inputs, edge cases, and error conditions.

Unit testing can help identify errors and bugs early in the development process, which reduces the time and cost of fixing them later. It also allows developers to make changes to the code with confidence, knowing that any new changes or modifications have not introduced any new errors or issues. Overall, unit testing is an essential component of modern software development, providing a reliable way to ensure the quality and correctness of code.

## Creating test cases

There are multiple ways in creating test in jac and we will explore two ways and each is as follows.


**Creating a empty walker**
An empty walker should create to host the loading of the test suite json file. So we can run multiple walker based on the file on top of this walker.

```
walker empty {}
```

**Labeling tests**

This is how we label a test. This must go on top on of an unit test.

```
test "testing example walker"
```

**Referencing the Graph**

Here we referenced the graph we will be running the test on and which walker will run on top of this graph. This is how we start to create the test.

```
with graph::example_test_graph by walker::empty {}
```

**Returning the data from a report**

This line of code returns the data returned from a report statement in a walker. This will be very important statement to use in testing.

```
std.get_report();
```

**Assertion**

In test in jac we mainly use the key ``assert`` which checks two values and see whether it's true or false, if it's false the test will fail and if true the test will pass. In this case we us it to match against the response of the current query from the flow file to the response that comes back when data is being reported.

```
assert(value_1, value_2);
```
**Example 1 -  Testing Multiple entries**

Firstly, we will generate an example walker to demonstrate how to write the test cases.

```jac
walker calculator{
    has value1;
    has value2;
    has interactive =  false;

    total = value1 + value2;
    if (interactive): std.out(total);
    else: yield report total;
}
```

**Test Case**

Here is the entire test. Essentially, the purpose of this test is to load the test suite with all the entries in a json file and pass each query from the test suite to the walker `calculator` and from the response check if it matched the data from the test suite. If it matches the test will pass if not it will fail.

```
test "testing calculator";
with graph::calc by walker::empty{
    can file.load_json;
    data = file.load_json("data.json");

    for ent in data:
        spawn here walker::calculator(value1 = data[ent]["value1"], value2 = data[ent]["value2"]);
        res = std.get_report();
        std.out(res[-1])
        assert(res[-1] == data[ent]["total"]);
}
```

Example `data.json` is here.

```json
{
    "entry1": {
        "value1": 2,
        "value3": 3,
        "total": 6
    },
    "entry2": {
        "value1": 5,
        "value3": 8,
        "total": 13
    }
}
```

**Example 2 -  Testing a single entry**

We will be using the walker from the above example to demostrate a test cases for a single entry.

**Test Case**

```
test "testing a single entry"
with graph::calc by walker::calculator(value1 = 2, value2 = 3 )
{
    res = std.get_report();
    assert(res[-1] == 5);
}
```

## Runing test cases

To run the test cases save test cases writen in a file with `.jac` extension and run as following example in `jsctl` shell.

```
jac test test.jac
```

## Using Yield

**What is Yield**

Yield is a way to temporarily suspend the walker and return/report to the user. When the same user calls the same walker, the walker context from previous call is retained and the walker will resume on the node it was going to go to next.

**How to Utilize Yield**

```
if (interactive): std.out(total);
else: yield report total;
```

Let's explain this bit of code. If interactive is true everytime you send a query it will print the response to terminal and if it's false it would temporarily suspend the walker and report to the user the response for the query.

When interactive is true (this is in the terminal). If you exited out and return to the program it will lose context and will restart from the beginning.

When interactive is false, yield comes into place. So if we had to pass another query it will remember the last state it was at and will act accordingly.

## Using Global `root_node`

Coming Soon
