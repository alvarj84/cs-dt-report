# CS-DT Report Tool

## Overview

The purpose of this tool is to generate a customer data report from Sysdig's API. The information presented in the generated report will be used to analyze customer's product usability.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)
7. [Acknowledgements](#acknowledgements)

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes. Please see the installation section for more information on how to get up and running.

The following is a UML use case diagram of the application:

![alt text](CS%20Report%20Tool.png)

## Prerequisites

To use the CS DT report tool, you will need the following:

- Python 3.7 or higher
- A working internet connection
- An API key from SDC Admin

## Installation

1. Clone the repo

```bash
git clone git@github.com:alvarj84/cs-dt-report.git
```

2. Change directory to the cloned repo

```bash
cd cs-dt-report
```

3. Install required packages using pip

```bash
pip install -r requirements.txt
```

4. Create a file named `sdc-admin-token` in the project's root directory and add the SDC Admin API key:

```bash
cat sdc-admin-token
808tyfd4-b311-46a6-9166-fa811a09196f%
```

## Usage

To run the CS DT Report tool, execute the following command in the project's root directory:

```bash
python report.py --customer_id 1005206 --region US2
```

Enter the customer id and the SaaS's region.

## Contributing

We welcome contributions from the community. If you would like to contribute, please follow these steps:

1. Fork the project repository.
2. Create a branch with a descriptive name that summarizes your changes.
3. Commit your changes to the branch.
4. Open a pull request against the original repository.

Please ensure that your code is well-documented and adheres to the existing style conventions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

- Jorge Alvarado (jorge.alvardo@sysdig.com)
- Diego Rodriguez (diego.rodriguez@sysdig.com)
