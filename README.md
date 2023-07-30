# Roblox Trade Cancel

Roblox Trade Cancel is a python application that automates the process of declining all inbound and outbound trade requests on Roblox.

## Getting Started

### Prerequisites

- Python
- The `requests` and `configparser` libraries. You can install these libraries using pip:
    ```bash
    pip install requests configparser
    ```

### Installation

1. Clone the repository
    ```bash
    git clone https://github.com/<your-github-username>/roblox-trade-cancel.git
    ```

2. Enter your directory
    ```bash
    cd roblox-trade-cancel
    ```

3. Create a `Config.ini` in the root directory with the following content and replace `replacewithyourcookie` with your Roblox cookie:
    ```ini
    [auth]
    cookie = replacewithyourcookie
    ```

4. Run the script
    ```bash
    python main.py
    ```

## Usage

Run the script, then choose whether to decline inbound or outbound trade requests by entering `1` or `2` respectively.

```python
[1] Inbounds
[2] Outbounds
Method: 
