package kevin.zhang;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.UnsupportedEncodingException;
import java.nio.charset.Charset;

/**
 * 对NLPIR的Java封装,便于Java程序员使用.<br/>
 * 
 * 注意:其中的函数名称及参数个数等与原函数有不同.
 * 
 * @author 陈海洋
 * @email 690732060@qq.com
 * @date 2013-5-29
 */
public class NLPIRJavaWraper {

	/**
	 * 计算所一级标注集
	 */
	public static final int POS_MAP_ICT_FIRST = 1;

	/**
	 * 计算所二级标注集
	 */
	public static final int POS_MAP_ICT_SECOND = 0;

	/**
	 * 北大二级标注集
	 */
	public static final int POS_MAP_PKU_SECOND = 2;

	/**
	 * 北大一级标注集
	 */
	public static final int POS_MAP_PKU_FIRST = 3;

	/**
	 *标记词性标记,用于paragraphProcess函数的POSTagged参数
	 */
	public static final int TAGGED_POS_YES = 1;

	/**
	 * 不标记词性,用于paragraphProcess函数的POSTagged参数
	 */
	public static final int TAGGED_POS_NO = 0;

	/**
	 * GB2312字符集名称常量
	 */
	public static final String ENCODING_GB2312 = "GB2312";

	/**
	 * UTF-8字符集名称常量
	 */
	public static final String ENCODING_UTF8 = "UTF-8";

	/**
	 * UTF-8字符集常量
	 */
	public static final Charset CHARSET_UTF8 = Charset.forName(ENCODING_UTF8);

	/**
	 * GB2312字符集常量
	 */
	public static final Charset CHARSET_GBK = Charset.forName(ENCODING_GB2312);

	/**
	 * GBK编码
	 */
	public static final int ENCODING_FLAG_GBK = 0;

	/**
	 * UTF-8编码
	 */
	public static final int ENCODING_FLAG_UTF8 = ENCODING_FLAG_GBK + 1;

	/**
	 * BIG5编码
	 */
	public static final int ENCODING_FLAG_BIG5 = 2;

	/**
	 *GBK编码(包含繁体)
	 */
	public static final int ENCODING_FLAG_GBK_FANTI = ENCODING_FLAG_GBK + 3;

	/**
	 * 实际调用的类
	 */
	private NLPIR nlpir = new NLPIR();

	private byte[] getBytes(String str) {
		return getBytes(str, ENCODING_GB2312);
	}

	private byte[] getBytes(String str, String encoding) {
		try {
			return str.getBytes(encoding);
		} catch (UnsupportedEncodingException e) {
			e.printStackTrace();
		}
		return null;
	}

	/**
	 * 默认的构造函数
	 */
	public NLPIRJavaWraper() {
		init("./file/");
	}

	/**
	 * 初始化
	 * 
	 * @param dataPath
	 *            Data文件夹路径,注意,是Data文件夹所在的文件夹,而非Data文件夹本身
	 * @param encodingFlag
	 *            编码标记,可选参数为: <br/>
	 *            ENCODING_FLAG_GBK GBK编码<br/>
	 *            ENCODING_FLAG_UTF8 UTF-8编码<br/>
	 *            ENCODING_FLAG_BIG5 BIG5编码<br/>
	 *            ENCODING_FLAG_GBK_FANTI GBK编码(包含繁体)<br/>
	 * 
	 * @return 如果初始化成功,返回true,否则返回false
	 */
	public void init(String dataDirectoryPath, int encodingFlag) {
		if (NLPIR.NLPIR_Init(getBytes(dataDirectoryPath), encodingFlag) == false) {
			throw new RuntimeException("初始化出错!");
		}
		System.out.println("初始化成功");
	}

	/**
	 * 初始化
	 * 
	 * @param dataPath
	 *            Data文件的路径
	 */
	public void init(String dataPath) {
		init(dataPath, ENCODING_FLAG_UTF8);
	}

	/**
	 * 退出
	 * 
	 * @return 如果成功返回true,否则返回false
	 */
	public static boolean exit() {
		return NLPIR.NLPIR_Exit();
	}

	/**
	 * 导入用户字典
	 * 
	 * @param path
	 *            用户字典路径
	 * @return 成功导入的词数
	 */
	public int importUserDict(File filePath) throws FileNotFoundException {
		return nlpir
				.NLPIR_ImportUserDict(filePath.getAbsolutePath().getBytes());
	}

	/**
	 * 获取是一个单字符的机率.<br/>
	 * 关于单字符(unigram)的解释参见http://baike.baidu.com/view/1219737.htm
	 * 
	 * @param word
	 *            要判断的词
	 * 
	 * @return 为一个unigram的机率
	 */
	public float getUnigramProbility(String word) {
		return nlpir.NLPIR_GetUniProb(getBytes(word));
	}

	/**
	 * 判断是否为一个单词
	 * 
	 * @param word
	 *            单词内容
	 * @return 如果是一个单词返回true,否则返回false
	 */
	public boolean isWord(String word) {
		return nlpir.NLPIR_IsWord(getBytes(word));
	}

	/**
	 * 处理一个段落<br/>
	 * 注意:默认会进行词性分析
	 * 
	 * @param str
	 *            段落
	 * @return 处理完成后的结果
	 */
	public String paragraphProcess(String str) {
		return paragraphProcess(str, true);
	}

	/**
	 * 处理段落
	 * 
	 * @param str
	 *            要被处理的字符串
	 * @param isHavePOS
	 *            是否包含词性,true为包含,false为不包含
	 * @return 处理过后的字符串
	 */
	public String paragraphProcess(String str, boolean isHavePOS) {
		if (str == null || str.length() == 0) {
			throw new IllegalArgumentException("输入的字符串为空");
		}

		try {
			return new String(nlpir.NLPIR_ParagraphProcess(getBytes(str,
					ENCODING_UTF8), isHavePOS ? 1 : 0), ENCODING_UTF8);
		} catch (UnsupportedEncodingException e) {
		}
		return null;
	}

	/**
	 * 文件处理
	 * 
	 * @param srcFile
	 *            源文件
	 * @param destFile
	 *            目标文件
	 * @return 如果成功返回true,否则返回false.
	 */
	public boolean fileProcess(File srcFile, File destFile) {
		return false;
	}

	/**
	 * 增加一个用户自定义的单词
	 * 
	 * @param word
	 *            单词
	 * @return 成功返回true,否则返回flase
	 */
	public boolean addUserWord(String word) {
		return nlpir.NLPIR_AddUserWord(getBytes(word)) == 1 ? true : false;
	}

	/**
	 * 保存用户词典到文件
	 * 
	 * @return
	 */
	public boolean saveUserDict() {
		// NLPIR_SaveTheUsrDic函数的返回值为1时为成功,2时为失败
		return nlpir.NLPIR_SaveTheUsrDic() == 1 ? true : false;
	}

	/**
	 * 删除一个用户自定义词
	 * 
	 * @param word
	 *            要删除的自定义词
	 * @return 成功返回true,否则返回flase
	 */
	public boolean deleteUserWord(String word) {
		return nlpir.NLPIR_DelUsrWord(getBytes(word)) == 1 ? true : false;
	}

	/**
	 * 设置词性标注集
	 * 
	 * @param nPOSMap
	 *            参数集,可选参数有: <br/>
	 *            POS_MAP_ICT_FIRST 计算所一级标注集 <br/>
	 *            POS_MAP_ICT_SECOND 计算所二级标注集<br/>
	 *            POS_MAP_PKU_SECOND 北大二级标注集 <br/>
	 *            POS_MAP_PKU_FIRST 北大一级标注集
	 * @return 如果成功则返回true,否则返回flase.
	 */
	public boolean setPOSMap(int nPOSMap) {
		return nlpir.NLPIR_SetPOSmap(nPOSMap) == 1 ? true : false;
	}

	/**
	 * 此函数未知
	 * 
	 * @param index
	 * @return
	 */
	public int getElementLength(int index) {
		// 此函数未知
		return 0;
	}

	public String getKeyWords(String str, int maxKeyLimit, boolean isHaveWeight) {
		return new String(nlpir.NLPIR_GetKeyWords(getBytes(str), maxKeyLimit,
				isHaveWeight));
	}

	/**
	 * 获取文件的关键字
	 * 
	 * @param fileName
	 *            文件路径
	 * @param maxKeyLimit
	 *            最大的键限制
	 * @param isHaveWeight
	 *            是否包含权重信息
	 * @return 处理完成后的字符串
	 */
	public String getFileKeyWords(String fileName, int maxKeyLimit,
			boolean isHaveWeight) {
		return new String(nlpir.NLPIR_GetFileKeyWords(getBytes(fileName),
				maxKeyLimit, isHaveWeight), Charset.forName(ENCODING_UTF8));
	}

	/**
	 * 从一个字符串获取新词
	 * 
	 * @param str
	 *            源字符串不
	 * @param maxKeyLimit
	 *            最大限制
	 * @param isHaveWeight
	 *            是否包含权重信息
	 * @return 处理完成后的字符串
	 */
	public String getNewWords(String str, int maxKeyLimit, boolean isHaveWeight) {
		return new String(nlpir.NLPIR_GetNewWords(getBytes(str), maxKeyLimit,
				isHaveWeight), Charset.forName(ENCODING_UTF8));
	}

	/**
	 * @param sFilename
	 * @param nMaxKeyLimit
	 * @param bWeightOut
	 * @return
	 */
	public String getFileNewWords(String str, int maxKeyLimit,
			boolean isHaveWeight) {
		return new String(nlpir.NLPIR_GetFileNewWords(getBytes(str),
				maxKeyLimit, isHaveWeight), Charset.forName(ENCODING_UTF8));
	}

	/*********************************************************************
	 * 
	 * 以下函数为2013版本专门针对新词发现的过程，一般建议脱机实现，不宜在线处理 新词识别完成后，再自动导入到分词系统中，即可完成
	 * 函数以NLPIR_NWI(New Word Identification)开头
	 *********************************************************************/
	/*********************************************************************
	 * 
	 * Func Name : NLPIR_NWI_Start
	 * 
	 * Description: 启动新词识别
	 * 
	 * 
	 * Parameters : None Returns : boolean, true:success, false:fail
	 * 
	 * Author : Kevin Zhang History : 1.create 2012/11/23
	 *********************************************************************/
	// New Word Indentification Start
	/**
	 * 
	 * 启动新词识别
	 * 
	 * @return true为成功,否则为flase
	 */
	public boolean startNewWordDetect() {
		return nlpir.NLPIR_NWI_Start();
	}

	/*********************************************************************
	 * 
	 * Func Name : NLPIR_NWI_AddFile
	 * 
	 * Description:
	 * 
	 * Parameters : byte[]sFilename：文件名 Returns : boolean, true:success,
	 * false:fail
	 * 
	 * Author : Kevin Zhang History : 1.create 2012/11/23
	 *********************************************************************/
	/**
	 * 往新词识别系统中添加待识别新词的文本文件 需要在运行start()之后，才有效
	 * 
	 * @param filePath
	 *            文件路径
	 * @return 如果成功返回true,否则返回false
	 */
	public boolean addNewWordFile(String filePath) {
		return nlpir.NLPIR_NWI_AddFile(getBytes(filePath)) == 1 ? true : false;
	}

	/**
	 * 往新词识别系统中添加一段待识别新词的内存 需要在运行NLPIR_NWI_Start()之后，才有效.
	 * 
	 * @param filePath
	 *            文件路径
	 * @return 如果成功返回true,否则返回false
	 */
	public boolean addTemporaryNewWordFile(String filePath) {
		return nlpir.NLPIR_NWI_AddMem(getBytes(filePath));
	}

	/**
	 * 新词识别添加内容结束 需要在运行NLPIR_NWI_Start()之后，才有效
	 * 
	 * @return 如果成功返回true,否则返回false
	 */
	public boolean complete() {
		return nlpir.NLPIR_NWI_Complete();
	}

	/**
	 * 获取新词识别的结果 需要在运行complete()之后，才有效.
	 * 
	 * @param isHaveWeight
	 *            是否需要输出每个新词的权重参数
	 * @return 结果字符串 ,输出格式为 【新词1】 【权重1】 【新词2】 【权重2】 ...
	 */
	public String getResult(boolean isHaveWeight) {
		return new String(nlpir.NLPIR_NWI_GetResult(isHaveWeight), CHARSET_UTF8);
	}

	/**
	 * 将新词识别结果导入到用户词典中 需要在运行NLPIR_NWI_Complete()之后，才有效.<br/>
	 * 如果需要将新词结果永久保存，建议在执行NLPIR_SaveTheUsrDic
	 * 
	 * @return 保存的单词个数
	 */
	public int resultToUserDict() {
		return nlpir.NLPIR_NWI_Result2UserDict();
	}
}
