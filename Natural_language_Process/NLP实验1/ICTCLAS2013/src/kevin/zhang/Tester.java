package kevin.zhang;

import java.util.List;

public class Tester {
	public static void main(String[] args) {
		NLPIRJavaWraper nlpUtil = new NLPIRJavaWraper();
		String result = nlpUtil.paragraphProcess("���ѽ,����һ������,����Ч��");

		System.out.println(result);

		List<WordEntry> wordEntries = WordEntryFactory.getWordEntries(result,
				true, false);

		System.out.println(wordEntries);
	}
}
