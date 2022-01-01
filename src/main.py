from configs import configs


def main():
    print(configs.API_KEY)
    print(configs.API_KEY.get_secret_value())


if __name__ == "__main__":
    main()
