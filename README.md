# AWS Lambda DynamoDB CRUD Function

This AWS Lambda function provides a RESTful API for performing CRUD (Create, Read, Update, Delete) operations on a DynamoDB table. It is designed to handle HTTP requests using AWS API Gateway.

## Table of Contents

- [Usage](#usage)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Usage

This Lambda function allows you to interact with a DynamoDB table through HTTP requests. It supports the following HTTP methods:

- GET: Retrieve data from the DynamoDB table.
- POST: Create a new item in the DynamoDB table.
- PUT: Update an existing item in the DynamoDB table.
- DELETE: Delete an item from the DynamoDB table.

## Dependencies

- [AWS Lambda](https://aws.amazon.com/lambda/): Serverless computing service.
- [AWS DynamoDB](https://aws.amazon.com/dynamodb/): Managed NoSQL database service.
- [AWS API Gateway](https://aws.amazon.com/api-gateway/): Create, publish, and manage APIs.

## Configuration

Before deploying this Lambda function, you need to configure:

1. AWS credentials and permissions.
2. DynamoDB table (e.g., 'MenuTable').

## API Endpoints

- **GET /menu**: Retrieve all items from the 'MenuTable'.
- **POST /menu**: Create a new item in the 'MenuTable'.
- **PUT /menu**: Update an existing item in the 'MenuTable'.
- **DELETE /menu?id={item_id}**: Delete an item from the 'MenuTable' by providing the 'item_id' as a query parameter.

## Deployment

1. Clone this repository.
2. Configure AWS credentials and permissions.
3. Create the DynamoDB table ('MenuTable') if it doesn't exist.
4. Deploy the Lambda function and configure API Gateway.
5. Test the API endpoints using appropriate tools (e.g., curl or Postman).

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a detailed description of your changes.


