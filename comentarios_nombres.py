import itertools
import configparser
import random

# Read configuration
config = configparser.ConfigParser()
config.read('config.ini')

# Read users_per_comment
users_per_comment = 2 # Default value
try:
    u_per_comment_str = config.get('General', 'users_per_comment')
    u_per_comment_int = int(u_per_comment_str)
    if u_per_comment_int >= 1:
        users_per_comment = u_per_comment_int
    else:
        print("Value for 'users_per_comment' in config.ini must be 1 or greater. Defaulting to 2.")
except (configparser.NoSectionError, configparser.NoOptionError):
    print("Missing 'users_per_comment' in config.ini under [General] section. Defaulting to 2.")
except ValueError:
    print(f"Invalid integer value for 'users_per_comment' ('{u_per_comment_str}') in config.ini. Defaulting to 2.")

# Read and parse custom_messages
custom_messages_str = config.get('General', 'custom_messages', fallback='')
parsed_messages = []
if custom_messages_str:
    parsed_messages = [msg.strip() for msg in custom_messages_str.split(',') if msg.strip()]

# Read usernames from usernames.txt
try:
    with open("usernames.txt", "r") as f:
        usernames = [line.strip() for line in f if line.strip()] # Ensure no empty lines are read
except FileNotFoundError:
    print("Error: usernames.txt not found. Please create it with one username per line.")
    usernames = []

combinaciones_formato = []

if not usernames:
    print("No usernames loaded. Cannot generate comments.")
elif len(usernames) < users_per_comment:
    print(f"Not enough usernames in usernames.txt (found {len(usernames)}) to create combinations of {users_per_comment} users.")
else:
    combinations = list(itertools.combinations(usernames, users_per_comment))
    for comb in combinations:
        current_comment_users = ' '.join([f'@{user}' for user in comb])
        if parsed_messages:
            random_message = random.choice(parsed_messages)
            final_comment = f"{current_comment_users} {random_message}"
        else:
            final_comment = current_comment_users
        combinaciones_formato.append(final_comment)

# Print the result (optional, for verification)
if combinaciones_formato:
    print(f"\nGenerated comments (for {users_per_comment} users per comment):")
    for combo_str in combinaciones_formato:
        print(combo_str)
else:
    print("\nNo comments were generated.")
