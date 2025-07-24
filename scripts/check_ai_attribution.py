#!/usr/bin/env python3
"""
Script to check AI attribution in git commits.
This helps ensure transparency in AI-assisted development.
"""

import subprocess
import sys
import re
from typing import List, Dict


def run_git_command(cmd: List[str]) -> str:
    """Run a git command and return the output."""
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running git command: {e}")
        return ""


def get_recent_commits(count: int = 10) -> List[Dict[str, str]]:
    """Get recent commit messages with their hashes."""
    cmd = ["git", "log", f"-{count}", "--pretty=format:%H|%s|%b"]
    output = run_git_command(cmd)
    
    commits = []
    for line in output.split('\n'):
        if '|' in line:
            parts = line.split('|', 2)
            if len(parts) >= 2:
                commit_hash = parts[0]
                subject = parts[1]
                body = parts[2] if len(parts) > 2 else ""
                
                commits.append({
                    'hash': commit_hash,
                    'subject': subject,
                    'body': body,
                    'full_message': f"{subject}\n{body}".strip()
                })
    
    return commits


def check_ai_attribution(commit_message: str) -> Dict[str, bool]:
    """Check if a commit message contains proper AI attribution."""
    message_lower = commit_message.lower()
    
    # AI tool mentions
    ai_tools = [
        'github copilot', 'copilot', 'chatgpt', 'gpt-4', 'gpt-3', 
        'claude', 'ai-assisted', 'ai-generated', 'ai assistance'
    ]
    
    # Attribution patterns
    attribution_patterns = [
        r'ai[- ]assistance:',
        r'ai[- ]generated:',
        r'copilot[- ]assisted:',
        r'human[- ]contribution:',
        r'ai[- ]review:',
        r'generated with',
        r'assisted by'
    ]
    
    has_ai_mention = any(tool in message_lower for tool in ai_tools)
    has_attribution = any(
        re.search(pattern, message_lower) for pattern in attribution_patterns
    )
    
    return {
        'has_ai_mention': has_ai_mention,
        'has_attribution': has_attribution,
        'needs_attribution': has_ai_mention and not has_attribution
    }


def main():
    """Main function to check AI attribution in recent commits."""
    print("🤖 Checking AI Attribution in Recent Commits")
    print("=" * 50)
    
    commits = get_recent_commits(10)
    
    if not commits:
        print("No commits found or error accessing git repository.")
        return
    
    issues_found = 0
    
    for commit in commits:
        attribution_check = check_ai_attribution(commit['full_message'])
        
        # Skip merge commits and automated commits
        if commit['subject'].startswith('Merge ') or 'automated' in commit['subject'].lower():
            continue
        
        print(f"\n📝 Commit: {commit['hash'][:8]}")
        print(f"   Subject: {commit['subject']}")
        
        if attribution_check['needs_attribution']:
            print("   ⚠️  WARNING: Commit mentions AI tools but lacks proper attribution")
            print("   💡 Consider adding attribution like:")
            print("      AI-Assistance: GitHub Copilot (code generation)")
            print("      Human-Contribution: Logic design, testing")
            issues_found += 1
        elif attribution_check['has_ai_mention'] and attribution_check['has_attribution']:
            print("   ✅ Good: Proper AI attribution found")
        else:
            print("   ℹ️  No AI assistance mentioned")
    
    print(f"\n📊 Summary:")
    print(f"   Commits checked: {len([c for c in commits if not c['subject'].startswith('Merge ')])}")
    print(f"   Attribution issues: {issues_found}")
    
    if issues_found > 0:
        print(f"\n⚠️  Found {issues_found} commits that may need better AI attribution.")
        print("   Consider updating commit messages or adding attribution in future commits.")
        
        # Don't fail the build for attribution issues, just warn
        # sys.exit(1)
    else:
        print("\n✅ All commits have appropriate AI attribution or no AI usage mentioned.")


if __name__ == "__main__":
    main()
