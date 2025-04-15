from datetime import datetime

class Post:
    def __init__(self, content, scheduled_time, platform):
        self.content = content
        self.scheduled_time = scheduled_time  # Expected to be a string in "YYYY-MM-DD HH:MM" format
        self.platform = platform

    def edit_content(self, new_content):
        self.content = new_content

    def change_scheduled_time(self, new_time):
        self.scheduled_time = new_time

    def display_post_details(self):
        print(f"Content: {self.content}\nScheduled Time: {self.scheduled_time}\nPlatform: {self.platform}\n")


class Scheduler:
    def __init__(self):
        self.posts = {}
        self.next_post_id = 1

    def add_post(self, post):
        post_id = self.next_post_id
        self.posts[post_id] = post
        self.next_post_id += 1
        print(f"Post added successfully with ID: {post_id}")

    def remove_post(self, post_id):
        if post_id in self.posts:
            del self.posts[post_id]
            print("Post removed successfully.")
        else:
            print("Post ID not found.")

    def view_all_posts(self):
        if not self.posts:
            print("No scheduled posts.")
        else:
            for post_id, post in self.posts.items():
                print(f"Post ID: {post_id}")
                post.display_post_details()

    def save_posts_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                for post_id, post in self.posts.items():
                    file.write(f"{post_id}|{post.content}|{post.scheduled_time}|{post.platform}\n")
            print("Posts saved successfully.")
        except Exception as e:
            print(f"Error saving posts to file: {e}")

    def load_posts_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    post_id, content, scheduled_time, platform = line.strip().split('|')
                    post = Post(content, scheduled_time, platform)
                    self.posts[int(post_id)] = post
                self.next_post_id = max(self.posts.keys(), default=0) + 1
            print("Posts loaded successfully.")
        except Exception as e:
            print(f"Error loading posts from file: {e}")


def menu():
    scheduler = Scheduler()

    while True:
        print("\nSocial Media Post Scheduler")
        print("1. Add New Post")
        print("2. Edit Post")
        print("3. Remove Post")
        print("4. View All Posts")
        print("5. Save Posts to File")
        print("6. Load Posts from File")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            content = input("Enter post content: ")
            scheduled_time = input("Enter scheduled time (YYYY-MM-DD HH:MM): ")
            platform = input("Enter platform (e.g., Twitter, Facebook): ")
            post = Post(content, scheduled_time, platform)
            scheduler.add_post(post)

        elif choice == '2':
            post_id = int(input("Enter Post ID to edit: "))
            if post_id in scheduler.posts:
                post = scheduler.posts[post_id]
                print("Enter new details (leave blank to skip):")
                new_content = input("New Content: ")
                new_scheduled_time = input("New Scheduled Time (YYYY-MM-DD HH:MM): ")

                if new_content:
                    post.edit_content(new_content)
                if new_scheduled_time:
                    post.change_scheduled_time(new_scheduled_time)

                print("Post updated successfully.")
            else:
                print("Post ID not found.")

        elif choice == '3':
            post_id = int(input("Enter Post ID to remove: "))
            scheduler.remove_post(post_id)

        elif choice == '4':
            scheduler.view_all_posts()

        elif choice == '5':
            filename = input("Enter filename to save posts: ")
            scheduler.save_posts_to_file(filename)

        elif choice == '6':
            filename = input("Enter filename to load posts: ")
            scheduler.load_posts_from_file(filename)

        elif choice == '7':
            print("Exiting Social Media Post Scheduler.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
