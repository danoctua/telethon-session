# Telethon Session Creator

This project will help you to quickly create a session you could reuse on any environment for authentication as a human user.

## Obtaining Telegram API Credentials

To create a session, you need to first obtain an application ID and hash for Telegram.

1. Visit [Telegram's API development tools](https://my.telegram.org/apps)
2. Create a new application
3. Obtain your App ID and App Hash

## Setting up

To setup the environment, please run the following command:
```bash
make setup
```

This command will:
- Prompt you to enter your Telegram App ID
- Prompt you to enter your Telegram App Hash
- Create a `.env` file with your credentials

## Running the Application

To build and run the application:

```bash
make run
```

This command will:
- Build the Docker image
- Run the container
- Mount the `sessions` directory
- Use credentials from the `.env` file
- Prompt you to enter a phone number
- Prompt you to enter verification code
- Prompt you to enter 2FA password (if set)

## Additional Commands

- `make build`: Build the Docker image
- `make setup-venv`: Installs required packages locally for development
- `make format`: Run pre-commit hooks for code formatting

## Security

- Credentials are stored in an isolated `.env` file
- Sessions are generated in the `sessions` directory
- Docker provides containerization for secure execution

## Troubleshooting

- Ensure Docker is installed and running
- Verify Telegram API credentials are correct
- Check network connectivity

## License

Refer to the [LICENSE](./LICENSE) file
