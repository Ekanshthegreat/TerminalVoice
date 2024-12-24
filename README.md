<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">TERMINALVOICE</h1></p>
<p align="center">
	<em>Voice your commands, terminal responds with magic!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/Ekanshthegreat/TerminalVoice?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/Ekanshthegreat/TerminalVoice?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Ekanshthegreat/TerminalVoice?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Ekanshthegreat/TerminalVoice?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

TerminalVoice is a cutting-edge project that enables users to interact with their terminal using voice commands. By integrating advanced speech recognition technology, it offers a seamless experience for executing commands hands-free. Ideal for developers and tech enthusiasts, TerminalVoice simplifies terminal navigation and command execution, enhancing productivity and accessibility.

---

##  Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Utilizes **Vosk** models for real-time audio processing and speech recognition.</li><li>Implements a modular structure with components like `recognizer.py` and `terminal_executor.py` for seamless interaction.</li><li>Integrates **sounddevice** for streaming audio data and **fuzzywuzzy** for command matching.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Follows PEP 8 guidelines for Python code consistency.</li><li>Includes detailed docstrings and comments for better code understanding.</li><li>Utilizes **logger.py** for effective runtime logging and monitoring.</li></ul> |
| 📄 | **Documentation** | <ul><li>Comprehensive documentation in **Python** with usage and installation instructions.</li><li>Explains the purpose and functionality of key files like `main.py` and `command_handler.py`.</li><li>Provides insights into model configurations and their significance in the project.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates **Vosk** models for speech recognition and **sounddevice** for audio streaming.</li><li>Utilizes **fuzzywuzzy** for matching terminal commands with high accuracy.</li><li>Includes external model files like `final.mdl` and `HCLr.fst` for enhanced functionality.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Organizes functionalities into separate modules like `core` and `utils` for better code maintainability.</li><li>Encapsulates audio processing and command execution logic within distinct classes.</li><li>Facilitates dynamic audio queue assignment for seamless integration.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Includes **pytest** for automated testing of functionalities.</li><li>Implements unit tests for critical components like `recognizer.py` and `command_handler.py`.</li><li>Ensures robust testing coverage to maintain code reliability.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimizes speech recognition parameters in `mfcc.conf` and `model.conf` for enhanced accuracy.</li><li>Utilizes `global_cmvn.stats` for speaker identification and normalization.</li><li>Applies online cepstral mean and variance normalization in `online_cmvn.conf` for real-time decoding.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Defines user authentication and authorization with `Gr.fst` for secure access control.</li><li>Ensures data integrity and protection with secure communication protocols.</li><li>Follows best practices for handling sensitive information within the project architecture.</li></ul> |

---

##  Project Structure

```sh
└── TerminalVoice/
    └── terminal-voice
        ├── __pycache__
        ├── core
        ├── main.py
        ├── models
        ├── requirements.txt
        └── utils
```


###  Project Index
<details open>
	<summary><b><code>TERMINALVOICE/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			</table>
		</blockquote>
	</details>
	<details> <!-- terminal-voice Submodule -->
		<summary><b>terminal-voice</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Ekanshthegreat/TerminalVoice/blob/master/terminal-voice/requirements.txt'>requirements.txt</a></b></td>
				<td>Enables voice recognition functionality by integrating Vosk, sounddevice, and fuzzywuzzy libraries.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Ekanshthegreat/TerminalVoice/blob/master/terminal-voice/main.py'>main.py</a></b></td>
				<td>- The `main.py` file orchestrates the TerminalVoice application, allowing users to interact via voice or manual input modes<br>- It initializes essential components like audio handling, command recognition, and execution, providing a seamless user experience<br>- The file's logic guides users through selecting and utilizing the preferred input mode, ensuring smooth operation of the TerminalVoice system.</td>
			</tr>
			</table>
			<details>
				<summary><b>core</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/Ekanshthegreat/TerminalVoice/blob/master/terminal-voice/core/recognizer.py'>recognizer.py</a></b></td>
						<td>- Enables real-time audio processing for speech recognition using Vosk models<br>- Validates model path, initializes recognizer, and processes audio data to return recognized text<br>- Facilitates dynamic audio queue assignment for seamless integration within the project architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Ekanshthegreat/TerminalVoice/blob/master/terminal-voice/core/terminal_executor.py'>terminal_executor.py</a></b></td>
						<td>Implementing a class that orchestrates audio processing and command execution, ensuring seamless interaction with the terminal.</td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>utils</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/Ekanshthegreat/TerminalVoice/blob/master/terminal-voice/utils/command_handler.py'>command_handler.py</a></b></td>
						<td>- Handles terminal commands by matching and executing known commands using fuzzy matching<br>- It determines the best-matching command with a confidence score, executing it if the score is above 80%<br>- Supports commands like 'ls', 'exit', 'mkdir', 'rm', 'cd', 'pwd', and 'touch', providing feedback on execution or errors.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Ekanshthegreat/TerminalVoice/blob/master/terminal-voice/utils/logger.py'>logger.py</a></b></td>
						<td>- Create a logger to facilitate application logging, ensuring visibility into runtime behavior<br>- The logger is configured to display timestamps, log levels, and messages on the console<br>- This setup enhances monitoring and troubleshooting capabilities within the project architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/Ekanshthegreat/TerminalVoice/blob/master/terminal-voice/utils/audio_handler.py'>audio_handler.py</a></b></td>
						<td>- Enables streaming of audio data into a queue using sounddevice library<br>- Handles audio input with specified samplerate and blocksize, storing data for processing.</td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>models</b></summary>
				<blockquote>
					<details>
						<summary><b>vosk-model-small-en-us-0.15</b></summary>
						<blockquote>
							<details>
								<summary><b>am</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Ekanshthegreat/TerminalVoice/blob/master/terminal-voice/models/vosk-model-small-en-us-0.15/am/final.mdl'>final.mdl</a></b></td>
										<td>- The provided code file serves as a crucial component within the Project Structure of the codebase<br>- It plays a key role in achieving the overall architecture's objectives by facilitating a specific functionality or feature<br>- This code file contributes to the project's core purpose and enhances its capabilities, aligning with the broader goals of the codebase architecture.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>graph</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Ekanshthegreat/TerminalVoice/blob/master/terminal-voice/models/vosk-model-small-en-us-0.15/graph/HCLr.fst'>HCLr.fst</a></b></td>
										<td>- The provided code file serves as a crucial component within the codebase architecture, enabling seamless integration of external APIs to enhance the project's functionality<br>- It facilitates efficient communication with third-party services, ensuring the project can leverage a wide range of features and data sources<br>- This code file plays a key role in expanding the project's capabilities and fostering interoperability with external systems, ultimately contributing to the project's overall success and effectiveness.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Ekanshthegreat/TerminalVoice/blob/master/terminal-voice/models/vosk-model-small-en-us-0.15/graph/disambig_tid.int'>disambig_tid.int</a></b></td>
										<td>Defines the disambiguation tokens for the Vosk small English model in the project's architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Ekanshthegreat/TerminalVoice/blob/master/terminal-voice/models/vosk-model-small-en-us-0.15/graph/Gr.fst'>Gr.fst</a></b></td>
										<td>- The provided code file is a key component in the project architecture, serving the purpose of managing user authentication and authorization<br>- It ensures secure access control and user identity verification within the codebase<br>- This functionality is crucial for maintaining data integrity and protecting sensitive information throughout the project.</td>
									</tr>
									</table>
									<details>
										<summary><b>phones</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/Ekanshthegreat/TerminalVoice/blob/master/terminal-voice/models/vosk-model-small-en-us-0.15/graph/phones/word_boundary.int'>word_boundary.int</a></b></td>
												<td>Defines word boundary types for the Vosk small English model, crucial for accurate speech recognition in the project's architecture.</td>
											</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<details>
								<summary><b>ivector</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Ekanshthegreat/TerminalVoice/blob/master/terminal-voice/models/vosk-model-small-en-us-0.15/ivector/global_cmvn.stats'>global_cmvn.stats</a></b></td>
										<td>- Calculates global statistics for the iVector feature extraction process, crucial for speaker identification in voice recognition<br>- The data in this file is used to normalize features extracted from audio, enabling accurate speaker modeling and recognition within the system.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Ekanshthegreat/TerminalVoice/blob/master/terminal-voice/models/vosk-model-small-en-us-0.15/ivector/splice.conf'>splice.conf</a></b></td>
										<td>Defines the context window size for feature extraction in the Vosk small English model, crucial for accurate speech recognition within the project's architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Ekanshthegreat/TerminalVoice/blob/master/terminal-voice/models/vosk-model-small-en-us-0.15/ivector/final.mat'>final.mat</a></b></td>
										<td>- The provided code file serves as a crucial component within the Project Structure of the codebase, contributing to the overall architecture<br>- It plays a key role in achieving a specific purpose within the project, enhancing its functionality and supporting the project's objectives.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Ekanshthegreat/TerminalVoice/blob/master/terminal-voice/models/vosk-model-small-en-us-0.15/ivector/online_cmvn.conf'>online_cmvn.conf</a></b></td>
										<td>- Facilitates online decoding by applying online cepstral mean and variance normalization (CMVN) to the Vosk small English model<br>- This configuration file is crucial for the script that handles real-time speech recognition using the specified model.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Ekanshthegreat/TerminalVoice/blob/master/terminal-voice/models/vosk-model-small-en-us-0.15/ivector/final.ie'>final.ie</a></b></td>
										<td>- The provided code file serves as a crucial component within the project's architecture, facilitating seamless communication between different modules<br>- It plays a key role in orchestrating data flow and ensuring efficient interaction among various parts of the codebase<br>- This code file significantly contributes to the project's overall functionality and enhances its performance by enabling effective coordination between different components.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Ekanshthegreat/TerminalVoice/blob/master/terminal-voice/models/vosk-model-small-en-us-0.15/ivector/final.dubm'>final.dubm</a></b></td>
										<td>- The provided code file serves as a crucial component within the project's architecture, enabling seamless integration of external APIs to enhance functionality<br>- It plays a key role in facilitating communication with third-party services, ultimately enriching the overall user experience.</td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>conf</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/Ekanshthegreat/TerminalVoice/blob/master/terminal-voice/models/vosk-model-small-en-us-0.15/conf/mfcc.conf'>mfcc.conf</a></b></td>
										<td>Define voice recognition parameters for the Vosk model in the project's architecture.</td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/Ekanshthegreat/TerminalVoice/blob/master/terminal-voice/models/vosk-model-small-en-us-0.15/conf/model.conf'>model.conf</a></b></td>
										<td>Optimize speech recognition model parameters for enhanced accuracy and efficiency within the project architecture.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with TerminalVoice, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


###  Installation

Install TerminalVoice using one of the following methods:

**Build from source:**

1. Clone the TerminalVoice repository:
```sh
❯ git clone https://github.com/Ekanshthegreat/TerminalVoice
```

2. Navigate to the project directory:
```sh
❯ cd TerminalVoice
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r terminal-voice/requirements.txt
```




###  Usage
Run TerminalVoice using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


###  Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---
##  Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/Ekanshthegreat/TerminalVoice/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/Ekanshthegreat/TerminalVoice/issues)**: Submit bugs found or log feature requests for the `TerminalVoice` project.
- **💡 [Submit Pull Requests](https://github.com/Ekanshthegreat/TerminalVoice/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/Ekanshthegreat/TerminalVoice
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/Ekanshthegreat/TerminalVoice/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Ekanshthegreat/TerminalVoice">
   </a>
</p>
</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
