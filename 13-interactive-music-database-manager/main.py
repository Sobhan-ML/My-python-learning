def add_user(username: str, age: int, city: str, albums: list, all_users: dict) -> None:
    """Registers a new user with their demographic data and album collection."""
    all_users[username] = {
        "age": age,
        "city": city,
        "albums": albums
    }


def add_album(name: str, artist: str, genre: str, tracks: int, all_albums: dict) -> None:
    """Registers a new album with its metadata."""
    all_albums[name] = {
        "artist": artist,
        "genre": genre,
        "tracks": tracks
    }


def query_user_artist(username: str, artist: str, all_users: dict, all_albums: dict) -> int:
    """Returns the total number of tracks a user has by a specific artist."""
    if username not in all_users:
        return 0

    return sum(
        all_albums[album]['tracks']
        for album in all_users[username]['albums']
        if album in all_albums and all_albums[album]['artist'] == artist
    )


def query_user_genre(username: str, genre: str, all_users: dict, all_albums: dict) -> int:
    """Returns the total number of tracks a user has in a specific genre."""
    if username not in all_users:
        return 0

    return sum(
        all_albums[album]['tracks']
        for album in all_users[username]['albums']
        if album in all_albums and all_albums[album]['genre'] == genre
    )


def query_age_artist(age: int, artist: str, all_users: dict, all_albums: dict) -> int:
    """Returns the total tracks by a specific artist owned by all users of a certain age."""
    return sum(
        all_albums[album]['tracks']
        for user_info in all_users.values() if user_info['age'] == age
        for album in user_info['albums']
        if album in all_albums and all_albums[album]['artist'] == artist
    )


def query_age_genre(age: int, genre: str, all_users: dict, all_albums: dict) -> int:
    """Returns the total tracks in a specific genre owned by all users of a certain age."""
    return sum(
        all_albums[album]['tracks']
        for user_info in all_users.values() if user_info['age'] == age
        for album in user_info['albums']
        if album in all_albums and all_albums[album]['genre'] == genre
    )


def query_city_artist(city: str, artist: str, all_users: dict, all_albums: dict) -> int:
    """Returns the total tracks by a specific artist owned by all users in a certain city."""
    return sum(
        all_albums[album]['tracks']
        for user_info in all_users.values() if user_info['city'] == city
        for album in user_info['albums']
        if album in all_albums and all_albums[album]['artist'] == artist
    )


def query_city_genre(city: str, genre: str, all_users: dict, all_albums: dict) -> int:
    """Returns the total tracks in a specific genre owned by all users in a certain city."""
    return sum(
        all_albums[album]['tracks']
        for user_info in all_users.values() if user_info['city'] == city
        for album in user_info['albums']
        if album in all_albums and all_albums[album]['genre'] == genre
    )


def main():
    print("========================================")
    print("Welcome to the Music Database Manager! 🎵")
    print("========================================")

    all_users = {}
    all_albums = {}

    while True:
        print("\n----------------------------------------")
        print("Menu Options:")
        print("1. Add Album")
        print("2. Add User")
        print("3. Query Tracks (User & Artist)")
        print("4. Query Tracks (User & Genre)")
        print("5. Query Tracks (Age & Artist)")
        print("6. Query Tracks (Age & Genre)")
        print("7. Query Tracks (City & Artist)")
        print("8. Query Tracks (City & Genre)")
        print("9. Exit")
        print("----------------------------------------")

        choice = input("Select an option (1-9): ").strip()

        # 1. Add Album
        if choice == '1':
            name = input("Enter album name: ").strip()
            artist = input("Enter artist name: ").strip()
            genre = input("Enter genre: ").strip()

            while True:
                try:
                    tracks = int(input("Enter number of tracks: ").strip())
                    if tracks <= 0:
                        print("❌ Error: Tracks count must be greater than 0.")
                        continue
                    break
                except ValueError:
                    print("❌ Warning: Please enter a valid number for tracks!")

            add_album(name, artist, genre, tracks, all_albums)
            print(f"✨ Album '{name}' added successfully!")

        # 2. Add User
        elif choice == '2':
            username = input("Enter username: ").strip()

            while True:
                try:
                    age = int(input("Enter user age: ").strip())
                    if age <= 0:
                        print("❌ Error: Age must be greater than 0.")
                        continue
                    break
                except ValueError:
                    print("❌ Warning: Please enter a valid number for age!")

            city = input("Enter city: ").strip()

            print(
                "Enter owned album names (separated by comma, e.g., Thriller, Abbey Road):")
            raw_albums = input("-> ").strip()
            albums_list = [alb.strip()
                           for alb in raw_albums.split(',') if alb.strip()]

            add_user(username, age, city, albums_list, all_users)
            print(f"✨ User '{username}' added successfully!")

        # 3. Query User & Artist
        elif choice == '3':
            user = input("Enter username: ").strip()
            artist = input("Enter artist name: ").strip()
            result = query_user_artist(user, artist, all_users, all_albums)
            print(f"\n-> Result: {result} tracks found. ✨")

        # 4. Query User & Genre
        elif choice == '4':
            user = input("Enter username: ").strip()
            genre = input("Enter genre: ").strip()
            result = query_user_genre(user, genre, all_users, all_albums)
            print(f"\n-> Result: {result} tracks found. ✨")

        # 5. Query Age & Artist
        elif choice == '5':
            while True:
                try:
                    age = int(input("Enter age: ").strip())
                    break
                except ValueError:
                    print("❌ Warning: Please enter a valid whole number for age!")
            artist = input("Enter artist name: ").strip()
            result = query_age_artist(age, artist, all_users, all_albums)
            print(f"\n-> Result: {result} tracks found. ✨")

        # 6. Query Age & Genre
        elif choice == '6':
            while True:
                try:
                    age = int(input("Enter age: ").strip())
                    break
                except ValueError:
                    print("❌ Warning: Please enter a valid whole number for age!")
            genre = input("Enter genre: ").strip()
            result = query_age_genre(age, genre, all_users, all_albums)
            print(f"\n-> Result: {result} tracks found. ✨")

        # 7. Query City & Artist
        elif choice == '7':
            city = input("Enter city: ").strip()
            artist = input("Enter artist name: ").strip()
            result = query_city_artist(city, artist, all_users, all_albums)
            print(f"\n-> Result: {result} tracks found. ✨")

        # 8. Query City & Genre
        elif choice == '8':
            city = input("Enter city: ").strip()
            genre = input("Enter genre: ").strip()
            result = query_city_genre(city, genre, all_users, all_albums)
            print(f"\n-> Result: {result} tracks found. ✨")

        # 9. Exit
        elif choice == '9':
            print("Exiting program... 🚀")
            break
        else:
            print("❌ Warning: Invalid option selected. Please choose between 1 and 9.")


if __name__ == "__main__":
    main()
