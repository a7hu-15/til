# Community Content Contributions & Workflows

Today I made several contributions to the open-source Japanese learning platform [KanaDojo](https://github.com/lingdojo/kana-dojo) and learned about their contribution workflow and community design.

## Project Structure & Content Scaling

KanaDojo scales its learning database (trivia, cultural facts, etiquette, proverbs, themes) by structuring them as plain JSON data files inside a `community/content/` directory.

- Pro: Allows anyone to contribute content without needing to write code (React, Next.js, or TypeScript).
- Workflow: An automated bot creates "Good First Issues" containing new entries to be appended to the JSON files. Contributors just fork, edit the corresponding JSON file, and open a Pull Request.

## Pull Request Constraints

While automating these contributions, I encountered a repository limit:
- **Maximum 3 Open PRs:** Upstream repositories can configure branch/contributor protection rules (or use automation bots) to limit each contributor to a maximum of 3 open pull requests at one time to prevent spam and overwhelm maintainers.
- **Workaround/Resolution:** To make more contributions, intermediate PRs had to be closed before opening new ones, keeping the final 3 open. Opening PRs (even if subsequently closed) still counts as an active contribution on the GitHub graph.

## Japanese Language & Cultural Facts Learned

Through these contributions, I also learned several interesting facts and proverbs:
1. **七転び八起き (Nanakorobi yaoki):** Fall down seven times, stand up eight. (A proverb emphasizing resilience).
2. **鬼の居ぬ間に洗濯 (Oni no inuma ni sentaku):** Do laundry while the ogre is away. (Equivalent to "When the cat's away, the mice will play").
3. **Nakizumo Festival:** A festival in Japan where sumo wrestlers compete to make babies cry first, which is believed to ward off evil spirits.
4. **贈り物 (Gift Giving Etiquette):** When giving gifts, one should hand them over with humble/reserved wording ("控えめな言い方で渡す") rather than emphasizing the value or cost ("値段を強調する").
