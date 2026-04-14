print(" Add, commit, push to GitHub")
import subprocess
import argparse

def run_command(command):
    print(f"\n>>> {command}\n")
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--message", help="Commit message")
    parser.add_argument("-f", "--force", action="store_true", help="Skip confirmation")

    args = parser.parse_args()

    # Default commit message
    message = args.message if args.message else "Updated files"

    print("git status:")
    run_command("git status")

    print("\nCommands to run:")
    print("git add .")
    print(f'git commit -m "{message}"')
    print("git push")

    if not args.force:
        confirm = input("\nRun these commands? (y/n): ")
        if confirm.lower() != "y":
            print("Cancelled.")
            return

    run_command("git add .")
    run_command(f'git commit -m "{message}"')
    run_command("git push")

if __name__ == "__main__":
    main()