1. Make sure you agree about formats and documentation
2. Start production it from Day 1 of the engagement
3. The client want to know:
	- Knowing the status of the security of the assets in scope
	- Knowing what is vulnerable
	- Knowing what need to be fixed first
4. The report needs to be:
	1. Exhaustive
	2. Clear
	3. On-time
	4. Good looking
	5. Adherent to client's goals
5. Understanding Your audience
	- The writing of report done simultaneously with testing
	- Do not stop the test to write the report but follow this process:
		- Process: Test & collect info => Finally write the report 
	1. __Executive Summary__:
		1. Engagement Summary
		2. At executive levels, you have to speak in terms of metrics, risk mitigation, and money loss.
		3. Graphs and statistics go here
	2. __IT Department__: 
		1. Here you can dive into more details about which areas or department are more affected and to what kind of vulnerabilities.
	3. __Development__:
		1. Here you provide your exploits your proofs of concepts, remediation tips, source code, etc.
		2. This is usually the most technical part of your report.
6. Tools to use
	1. Xmind
7. The Report structure
	1. Executive Summary
		1. Where you talk to the corporate types or, in general, give a brief and concise overview about the whole engagement.
		2. No more than 2-3 pages
		3. An introduction to the Executive summary could read like this:
			1. "The purpose of this assessment and report is to identify any web application issues that could after ABC, Inc.'s e-commerce application and the web server hosting it, and to provide solutions to remedy these same issues.'"
		4. Use Graph
			1. Vulnerabilities by impact: ![[0. Official WORK & notes/Penetration testing/Photos/1.png]]
			2. Successful Attacks By Type:![[0. Official WORK & notes/Penetration testing/Photos/3.png]]
			3. You can create a similar graphs with: http://projects.webappsec.org/w/page/13246978/Threat%20Classification
	2. Vulnerability Report
		1. Called also "Technical Report"
		2. To introduce this chapter you can use graphs of number of vulnerabilities by categories (sql -> 2 , XSS -> 1, ... etc)
		3. New Section: Vulnerability by Type (concentrate more on vulnerability more than the target itself)
			1. You should use a schema like this:![[0. Official WORK & notes/Penetration testing/Photos/4.png]]
			2. Description of vulnerabilities can be taken from:
				1. NIST
				2. OSVDB (https://cve.mitre.org/data/refs/refmap/source-OSVDB.html)
			3. You can add further explanation when the description sounds meaningless or is too generic. (Make sure the description is always relevant to your client environment)
			4. Impact Value: beside the name of the vulnerability, you should also assign an impact value using (You can use OWASP TOP 10):
				1. Difficulty of exploitation: How hard was it? Easy?
				2. Affected Systems: According to their asset value
				3. Exposure:
					- Is it a remote vulnerability? Local?
					- Does it require a privileged account? ...
				4. Availability: 
					- Is there a public exploit?
					- A Metasploit module?
	3. Remediation Report
		1. Place to talk to developers in charge of fixing the vulnerabilities
		2. We work on 2 time horizons:
			1. __Short term__: 
				1. Remediation the team to address the most important vulnerabilities as soon as possible.
				2. Your client can provide a emergency phone number where you can immediately call a developer
				3. Duration: Weeks -> months
				4. __Long term__:
					1. Implementation of SSDLC (Secure Software Development Lifecycle)
					2. The employment of security checks early in the business or development processes
					3. Or the use of different platforms, versions or frameworks.
					4. Duration: 6 -> 12 months
		3. Provide suggestion on how to remediate common vulnerabilities (if available or net reference available patches, upgrades, hotfixes .. etc)
		4. Prioritize your remediation plan according to the impact level
		5. Templates and guides: 
			1. https://cure53.de/#publications
