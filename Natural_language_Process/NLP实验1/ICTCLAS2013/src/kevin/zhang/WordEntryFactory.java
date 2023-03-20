package kevin.zhang;

import java.util.LinkedList;
import java.util.List;

/**
 * WordEntry生成工厂
 * 
 * @author NightRunner
 * @email 690732060@qq.com
 * @history 1.create 2013-5-29
 * 
 */
public class WordEntryFactory {

	/**
	 * 根据字符串生成词条对象List
	 * 
	 * @param str
	 *            字符串.
	 *            例如:"你/rr 好/a 呀/y ,/wd 这/rzv 是/vshi 一个/mq 测试/vn ,/wd 看看/v 效果/n"
	 * @param isHavePOS
	 *            是否包含有词性
	 * @param isHaveWeight
	 *            是否包含权重
	 * @return WordEntry的List集合
	 */
	public static List<WordEntry> getWordEntries(String str, boolean isHavePOS,
			boolean isHaveWeight) {
		List<WordEntry> wordEntries = new LinkedList<WordEntry>();

		String[] wordUnits = str.split(" ");
		String[] temp = null;
		WordEntry wordEntry = null;

		for (String wordUnit : wordUnits) {

			// 最后一个字符为0,不处理
			if (wordUnit.charAt(0) == 0) {
				continue;
			}

			temp = wordUnit.split("/");

			wordEntry = new WordEntry();

			wordEntry.setWord(temp[0]);
			if (isHavePOS) {
				wordEntry.setPartOfSpeech(temp[1]);
			}

			if (isHaveWeight) {
				wordEntry.setWeight(Float.parseFloat(temp[3]));
			}

			wordEntries.add(wordEntry);
		}

		return wordEntries;
	}
}