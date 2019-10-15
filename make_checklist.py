
def isCheckList(line):
    return line.trim().starts_with("* [ ] ")


def create_checklist():
    lines = list("MobProgrammingFacilitorsGuide_English.md")
    checklist = filter(isCheckList, lines)
    outF = open("MobProgrammingFacilitors.Checklist.md", "w")
    outF.writelines(checklist)
    outF.close()

'''
	@Test
	public void testName() throws Exception {
		String file = "/Users/llewellyn/GitHub/MobProgrammingFacilitatorsGuide/MobProgrammingFacilitorsGuide_English.md";
		String text = FileUtils.readFile(file);
		String[] lines = text.split("\n");
		List<String> checklist = Query.where(lines, l -> l.startsWith("* [ ] ") || l.startsWith("## "));
		String output = StringUtils.join(checklist, "\n");
		File outputFile = new File(file.replaceAll("\\.md", "\\.checklist\\.md"));
		FileUtils.writeFile(outputFile, output);
		TestUtils.displayFile(outputFile.getAbsolutePath());
	}
'''