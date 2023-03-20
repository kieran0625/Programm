package kevin.zhang;

/**
 * 词条对象
 * 
 * @author NightRunner
 * 
 */
public class WordEntry {

	/**
	 * 词
	 */
	private String word;

	/**
	 *词性
	 */
	private String partOfSpeech;

	/**
	 * 权重
	 */
	private float weight;

	/**
	 * 是否设置过weight
	 */
	private boolean isSetedWeight = false;

	/**
	 * 是否设置过 partOfSpeech
	 */
	private boolean isSetedPartOfSpeech = false;

	public float getWeight() {
		return weight;
	}

	public void setWeight(float weight) {
		this.weight = weight;
		isSetedWeight = true;
	}

	public String getPartOfSpeech() {
		return partOfSpeech;
	}

	public void setPartOfSpeech(String partOfSpeech) {
		this.partOfSpeech = partOfSpeech;
		isSetedPartOfSpeech = true;
	}

	public WordEntry() {
	}

	public WordEntry(String word) {
		setWord(word);
	}

	public WordEntry(String word, String partOfSppeech) {
		setWord(word);
		setPartOfSpeech(partOfSppeech);
	}

	public WordEntry(String word, String partOfSppeech, float weight) {
		setWord(word);
		setPartOfSpeech(partOfSppeech);
		setWeight(weight);
	}

	public String getWord() {
		return word;
	}

	public void setWord(String word) {
		this.word = word;
	}

	public String toString() {
		StringBuffer buffer = new StringBuffer();

		buffer.append(word);

		if (isSetedPartOfSpeech) {
			buffer.append("/");
			buffer.append(partOfSpeech);
		}

		if (isSetedWeight) {
			buffer.append("/");
			buffer.append(weight);
		}

		return buffer.toString();
	}
}