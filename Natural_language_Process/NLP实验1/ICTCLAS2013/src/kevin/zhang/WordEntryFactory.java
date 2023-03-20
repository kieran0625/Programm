package kevin.zhang;

import java.util.LinkedList;
import java.util.List;

/**
 * WordEntry���ɹ���
 * 
 * @author NightRunner
 * @email 690732060@qq.com
 * @history 1.create 2013-5-29
 * 
 */
public class WordEntryFactory {

	/**
	 * �����ַ������ɴ�������List
	 * 
	 * @param str
	 *            �ַ���.
	 *            ����:"��/rr ��/a ѽ/y ,/wd ��/rzv ��/vshi һ��/mq ����/vn ,/wd ����/v Ч��/n"
	 * @param isHavePOS
	 *            �Ƿ�����д���
	 * @param isHaveWeight
	 *            �Ƿ����Ȩ��
	 * @return WordEntry��List����
	 */
	public static List<WordEntry> getWordEntries(String str, boolean isHavePOS,
			boolean isHaveWeight) {
		List<WordEntry> wordEntries = new LinkedList<WordEntry>();

		String[] wordUnits = str.split(" ");
		String[] temp = null;
		WordEntry wordEntry = null;

		for (String wordUnit : wordUnits) {

			// ���һ���ַ�Ϊ0,������
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