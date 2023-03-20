package kevin.zhang;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.UnsupportedEncodingException;
import java.nio.charset.Charset;

/**
 * ��NLPIR��Java��װ,����Java����Աʹ��.<br/>
 * 
 * ע��:���еĺ������Ƽ�������������ԭ�����в�ͬ.
 * 
 * @author �º���
 * @email 690732060@qq.com
 * @date 2013-5-29
 */
public class NLPIRJavaWraper {

	/**
	 * ������һ����ע��
	 */
	public static final int POS_MAP_ICT_FIRST = 1;

	/**
	 * ������������ע��
	 */
	public static final int POS_MAP_ICT_SECOND = 0;

	/**
	 * ���������ע��
	 */
	public static final int POS_MAP_PKU_SECOND = 2;

	/**
	 * ����һ����ע��
	 */
	public static final int POS_MAP_PKU_FIRST = 3;

	/**
	 *��Ǵ��Ա��,����paragraphProcess������POSTagged����
	 */
	public static final int TAGGED_POS_YES = 1;

	/**
	 * ����Ǵ���,����paragraphProcess������POSTagged����
	 */
	public static final int TAGGED_POS_NO = 0;

	/**
	 * GB2312�ַ������Ƴ���
	 */
	public static final String ENCODING_GB2312 = "GB2312";

	/**
	 * UTF-8�ַ������Ƴ���
	 */
	public static final String ENCODING_UTF8 = "UTF-8";

	/**
	 * UTF-8�ַ�������
	 */
	public static final Charset CHARSET_UTF8 = Charset.forName(ENCODING_UTF8);

	/**
	 * GB2312�ַ�������
	 */
	public static final Charset CHARSET_GBK = Charset.forName(ENCODING_GB2312);

	/**
	 * GBK����
	 */
	public static final int ENCODING_FLAG_GBK = 0;

	/**
	 * UTF-8����
	 */
	public static final int ENCODING_FLAG_UTF8 = ENCODING_FLAG_GBK + 1;

	/**
	 * BIG5����
	 */
	public static final int ENCODING_FLAG_BIG5 = 2;

	/**
	 *GBK����(��������)
	 */
	public static final int ENCODING_FLAG_GBK_FANTI = ENCODING_FLAG_GBK + 3;

	/**
	 * ʵ�ʵ��õ���
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
	 * Ĭ�ϵĹ��캯��
	 */
	public NLPIRJavaWraper() {
		init("./file/");
	}

	/**
	 * ��ʼ��
	 * 
	 * @param dataPath
	 *            Data�ļ���·��,ע��,��Data�ļ������ڵ��ļ���,����Data�ļ��б���
	 * @param encodingFlag
	 *            ������,��ѡ����Ϊ: <br/>
	 *            ENCODING_FLAG_GBK GBK����<br/>
	 *            ENCODING_FLAG_UTF8 UTF-8����<br/>
	 *            ENCODING_FLAG_BIG5 BIG5����<br/>
	 *            ENCODING_FLAG_GBK_FANTI GBK����(��������)<br/>
	 * 
	 * @return �����ʼ���ɹ�,����true,���򷵻�false
	 */
	public void init(String dataDirectoryPath, int encodingFlag) {
		if (NLPIR.NLPIR_Init(getBytes(dataDirectoryPath), encodingFlag) == false) {
			throw new RuntimeException("��ʼ������!");
		}
		System.out.println("��ʼ���ɹ�");
	}

	/**
	 * ��ʼ��
	 * 
	 * @param dataPath
	 *            Data�ļ���·��
	 */
	public void init(String dataPath) {
		init(dataPath, ENCODING_FLAG_UTF8);
	}

	/**
	 * �˳�
	 * 
	 * @return ����ɹ�����true,���򷵻�false
	 */
	public static boolean exit() {
		return NLPIR.NLPIR_Exit();
	}

	/**
	 * �����û��ֵ�
	 * 
	 * @param path
	 *            �û��ֵ�·��
	 * @return �ɹ�����Ĵ���
	 */
	public int importUserDict(File filePath) throws FileNotFoundException {
		return nlpir
				.NLPIR_ImportUserDict(filePath.getAbsolutePath().getBytes());
	}

	/**
	 * ��ȡ��һ�����ַ��Ļ���.<br/>
	 * ���ڵ��ַ�(unigram)�Ľ��Ͳμ�http://baike.baidu.com/view/1219737.htm
	 * 
	 * @param word
	 *            Ҫ�жϵĴ�
	 * 
	 * @return Ϊһ��unigram�Ļ���
	 */
	public float getUnigramProbility(String word) {
		return nlpir.NLPIR_GetUniProb(getBytes(word));
	}

	/**
	 * �ж��Ƿ�Ϊһ������
	 * 
	 * @param word
	 *            ��������
	 * @return �����һ�����ʷ���true,���򷵻�false
	 */
	public boolean isWord(String word) {
		return nlpir.NLPIR_IsWord(getBytes(word));
	}

	/**
	 * ����һ������<br/>
	 * ע��:Ĭ�ϻ���д��Է���
	 * 
	 * @param str
	 *            ����
	 * @return ������ɺ�Ľ��
	 */
	public String paragraphProcess(String str) {
		return paragraphProcess(str, true);
	}

	/**
	 * �������
	 * 
	 * @param str
	 *            Ҫ��������ַ���
	 * @param isHavePOS
	 *            �Ƿ��������,trueΪ����,falseΪ������
	 * @return ���������ַ���
	 */
	public String paragraphProcess(String str, boolean isHavePOS) {
		if (str == null || str.length() == 0) {
			throw new IllegalArgumentException("������ַ���Ϊ��");
		}

		try {
			return new String(nlpir.NLPIR_ParagraphProcess(getBytes(str,
					ENCODING_UTF8), isHavePOS ? 1 : 0), ENCODING_UTF8);
		} catch (UnsupportedEncodingException e) {
		}
		return null;
	}

	/**
	 * �ļ�����
	 * 
	 * @param srcFile
	 *            Դ�ļ�
	 * @param destFile
	 *            Ŀ���ļ�
	 * @return ����ɹ�����true,���򷵻�false.
	 */
	public boolean fileProcess(File srcFile, File destFile) {
		return false;
	}

	/**
	 * ����һ���û��Զ���ĵ���
	 * 
	 * @param word
	 *            ����
	 * @return �ɹ�����true,���򷵻�flase
	 */
	public boolean addUserWord(String word) {
		return nlpir.NLPIR_AddUserWord(getBytes(word)) == 1 ? true : false;
	}

	/**
	 * �����û��ʵ䵽�ļ�
	 * 
	 * @return
	 */
	public boolean saveUserDict() {
		// NLPIR_SaveTheUsrDic�����ķ���ֵΪ1ʱΪ�ɹ�,2ʱΪʧ��
		return nlpir.NLPIR_SaveTheUsrDic() == 1 ? true : false;
	}

	/**
	 * ɾ��һ���û��Զ����
	 * 
	 * @param word
	 *            Ҫɾ�����Զ����
	 * @return �ɹ�����true,���򷵻�flase
	 */
	public boolean deleteUserWord(String word) {
		return nlpir.NLPIR_DelUsrWord(getBytes(word)) == 1 ? true : false;
	}

	/**
	 * ���ô��Ա�ע��
	 * 
	 * @param nPOSMap
	 *            ������,��ѡ������: <br/>
	 *            POS_MAP_ICT_FIRST ������һ����ע�� <br/>
	 *            POS_MAP_ICT_SECOND ������������ע��<br/>
	 *            POS_MAP_PKU_SECOND ���������ע�� <br/>
	 *            POS_MAP_PKU_FIRST ����һ����ע��
	 * @return ����ɹ��򷵻�true,���򷵻�flase.
	 */
	public boolean setPOSMap(int nPOSMap) {
		return nlpir.NLPIR_SetPOSmap(nPOSMap) == 1 ? true : false;
	}

	/**
	 * �˺���δ֪
	 * 
	 * @param index
	 * @return
	 */
	public int getElementLength(int index) {
		// �˺���δ֪
		return 0;
	}

	public String getKeyWords(String str, int maxKeyLimit, boolean isHaveWeight) {
		return new String(nlpir.NLPIR_GetKeyWords(getBytes(str), maxKeyLimit,
				isHaveWeight));
	}

	/**
	 * ��ȡ�ļ��Ĺؼ���
	 * 
	 * @param fileName
	 *            �ļ�·��
	 * @param maxKeyLimit
	 *            ���ļ�����
	 * @param isHaveWeight
	 *            �Ƿ����Ȩ����Ϣ
	 * @return ������ɺ���ַ���
	 */
	public String getFileKeyWords(String fileName, int maxKeyLimit,
			boolean isHaveWeight) {
		return new String(nlpir.NLPIR_GetFileKeyWords(getBytes(fileName),
				maxKeyLimit, isHaveWeight), Charset.forName(ENCODING_UTF8));
	}

	/**
	 * ��һ���ַ�����ȡ�´�
	 * 
	 * @param str
	 *            Դ�ַ�����
	 * @param maxKeyLimit
	 *            �������
	 * @param isHaveWeight
	 *            �Ƿ����Ȩ����Ϣ
	 * @return ������ɺ���ַ���
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
	 * ���º���Ϊ2013�汾ר������´ʷ��ֵĹ��̣�һ�㽨���ѻ�ʵ�֣��������ߴ��� �´�ʶ����ɺ����Զ����뵽�ִ�ϵͳ�У��������
	 * ������NLPIR_NWI(New Word Identification)��ͷ
	 *********************************************************************/
	/*********************************************************************
	 * 
	 * Func Name : NLPIR_NWI_Start
	 * 
	 * Description: �����´�ʶ��
	 * 
	 * 
	 * Parameters : None Returns : boolean, true:success, false:fail
	 * 
	 * Author : Kevin Zhang History : 1.create 2012/11/23
	 *********************************************************************/
	// New Word Indentification Start
	/**
	 * 
	 * �����´�ʶ��
	 * 
	 * @return trueΪ�ɹ�,����Ϊflase
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
	 * Parameters : byte[]sFilename���ļ��� Returns : boolean, true:success,
	 * false:fail
	 * 
	 * Author : Kevin Zhang History : 1.create 2012/11/23
	 *********************************************************************/
	/**
	 * ���´�ʶ��ϵͳ����Ӵ�ʶ���´ʵ��ı��ļ� ��Ҫ������start()֮�󣬲���Ч
	 * 
	 * @param filePath
	 *            �ļ�·��
	 * @return ����ɹ�����true,���򷵻�false
	 */
	public boolean addNewWordFile(String filePath) {
		return nlpir.NLPIR_NWI_AddFile(getBytes(filePath)) == 1 ? true : false;
	}

	/**
	 * ���´�ʶ��ϵͳ�����һ�δ�ʶ���´ʵ��ڴ� ��Ҫ������NLPIR_NWI_Start()֮�󣬲���Ч.
	 * 
	 * @param filePath
	 *            �ļ�·��
	 * @return ����ɹ�����true,���򷵻�false
	 */
	public boolean addTemporaryNewWordFile(String filePath) {
		return nlpir.NLPIR_NWI_AddMem(getBytes(filePath));
	}

	/**
	 * �´�ʶ��������ݽ��� ��Ҫ������NLPIR_NWI_Start()֮�󣬲���Ч
	 * 
	 * @return ����ɹ�����true,���򷵻�false
	 */
	public boolean complete() {
		return nlpir.NLPIR_NWI_Complete();
	}

	/**
	 * ��ȡ�´�ʶ��Ľ�� ��Ҫ������complete()֮�󣬲���Ч.
	 * 
	 * @param isHaveWeight
	 *            �Ƿ���Ҫ���ÿ���´ʵ�Ȩ�ز���
	 * @return ����ַ��� ,�����ʽΪ ���´�1�� ��Ȩ��1�� ���´�2�� ��Ȩ��2�� ...
	 */
	public String getResult(boolean isHaveWeight) {
		return new String(nlpir.NLPIR_NWI_GetResult(isHaveWeight), CHARSET_UTF8);
	}

	/**
	 * ���´�ʶ�������뵽�û��ʵ��� ��Ҫ������NLPIR_NWI_Complete()֮�󣬲���Ч.<br/>
	 * �����Ҫ���´ʽ�����ñ��棬������ִ��NLPIR_SaveTheUsrDic
	 * 
	 * @return ����ĵ��ʸ���
	 */
	public int resultToUserDict() {
		return nlpir.NLPIR_NWI_Result2UserDict();
	}
}
