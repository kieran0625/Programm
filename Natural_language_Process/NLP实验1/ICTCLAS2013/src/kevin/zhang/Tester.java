package kevin.zhang;

import java.util.List;

public class Tester {
	public static void main(String[] args) {
		NLPIRJavaWraper nlpUtil = new NLPIRJavaWraper();
		String result = nlpUtil.paragraphProcess("你好呀,这是一个测试,看看效果");

		System.out.println(result);

		List<WordEntry> wordEntries = WordEntryFactory.getWordEntries(result,
				true, false);

		System.out.println(wordEntries);
	}
}
