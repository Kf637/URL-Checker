# URL Checker

This project is a simple URL checker that reads URLs from a file, checks their HTTP status codes, and prints the results. It uses threading to perform the checks concurrently, making the process faster.

## Configuration

The configuration settings are defined at the beginning of the `main.py` file:

- `timeout`: Timeout in seconds for each URL check.
- `allow_redirects`: Boolean indicating whether to allow redirects.
- `urls_file`: The file containing the list of URLs to check.
- `http_codes_file`: The file containing the list of allowed HTTP status codes.

## ANSI Escape Codes

The script uses ANSI escape codes for colored output:

- `GREEN`: Indicates a successful check.
- `RED`: Indicates an error or timeout.

## Usage

1. **Prepare the URLs file**: Create a file named `urls.txt` and list the URLs to be checked, separated by commas.

    Example:
    ```
    example.com, google.com, github.com
    ```

2. **Prepare the HTTP codes file**: Create a file named [`httpcodes.txt`] and list the allowed HTTP status codes, separated by commas.

    Example:
    ```
    200, 301, 302
    ```

3. **Run the script**: Execute the [`main.py`] script to start the URL checking process.

    ```sh
    python main.py
    ```

## Output

The script will print the current configuration and start checking the URLs. It will output the status of each URL, indicating whether it is successful or if there was an error.

Example output:
```
Current configuration:

Timeout: 1 seconds
Allow redirects: True
URLs: urls.txt
Allowed HTTP codes: httpcodes.txt
ANSI codes: Green Red Reset

------- STARTING ------- 
Checking domain: example.com 
200 found for example.com 
Checking domain: google.com 
200 found for google.com 
Checking domain: github.com 
200 found for github.com 

------- DONE ------- 
Successful URLs: 
example.com 
google.com 
github.com
```


## Dependencies

- [`requests`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Ffredr%2FDesktop%2FCode%2FHTTPrequest%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A7%7D%7D%5D%2C%22f8aaa457-ea69-4bf2-bd52-9869db7ff878%22%5D "Go to definition"): For making HTTP requests.
- [`threading`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Ffredr%2FDesktop%2FCode%2FHTTPrequest%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A7%7D%7D%5D%2C%22f8aaa457-ea69-4bf2-bd52-9869db7ff878%22%5D "Go to definition"): For concurrent URL checking.
- [`os`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Ffredr%2FDesktop%2FCode%2FHTTPrequest%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A2%2C%22character%22%3A7%7D%7D%5D%2C%22f8aaa457-ea69-4bf2-bd52-9869db7ff878%22%5D "Go to definition"): For system operations like clearing the console and checking file existence.

Install the required dependencies using pip:

```sh
pip install requests
```

# License
This project is licensed under the MIT License.

This [`README.md`] file provides an overview of the project, configuration details, usage instructions, and example output.

