package kevin.zhang;

import java.io.UnsupportedEncodingException;

import kevin.zhang.NLPIR;

public class TestNLPIR {

	public static void main(String[] args) throws Exception {
		try {
			String sInput = "Ѹ�ٵ��Ƴ���NLPIR�ִ�ϵͳ������ICTCLAS2013�������´�ʶ�𡢹ؼ�����ȡ��΢���ִʹ���.";

			// ����Ӧ�ִ�
			test(sInput);

		} catch (Exception ex) {
			ex.printStackTrace();
		}
	}

	public static byte[] getBytes(String str) {
		return getBytes(str, "GB2312");
	}

	public static byte[] getBytes(String str, String encoding) {
		try {
			return str.getBytes(encoding);
		} catch (UnsupportedEncodingException e) {
			e.printStackTrace();
		}
		return null;
	}

	public static void test(String sInput) {
		try {
			NLPIR testNLPIR = new NLPIR();

			String dataDirectoryPath = "./file/";
			System.out.println("NLPIR_Init");
			if (testNLPIR.NLPIR_Init(getBytes(dataDirectoryPath), 1) == false) {
				System.out.println("Init Fail!");
				return;
			}

			// �����û��ʵ�ǰ
			byte nativeBytes[] = testNLPIR.NLPIR_ParagraphProcess(
					getBytes(sInput), 1);
			String nativeStr = new String(nativeBytes, 0, nativeBytes.length,
					"UTF-8");

			System.out.println("�ִʽ��Ϊ�� " + nativeStr);

			// ��ʼ���ִ����
			String inputFilePath = "./test/test.TXT";
			String outputFilePath = "./test/test_result1.TXT";

			nativeBytes = testNLPIR.NLPIR_GetFileNewWords(inputFilePath
					.getBytes("GB2312"), 50, true);

			// ����Ǵ����ڴ棬���Ե���testNLPIR.NLPIR_GetNewWords
			nativeStr = new String(nativeBytes, 0, nativeBytes.length, "UTF-8");
			System.out.println("�´�ʶ����Ϊ�� " + nativeStr);

			nativeBytes = testNLPIR.NLPIR_GetFileKeyWords(
					getBytes(inputFilePath), 50, true);
			// ����Ǵ����ڴ棬���Ե���testNLPIR.NLPIR_GetKeyWords
			nativeStr = new String(nativeBytes, 0, nativeBytes.length, "UTF-8");
			System.out.println("�ؼ���ʶ����Ϊ�� " + nativeStr);

			testNLPIR.NLPIR_FileProcess(getBytes(inputFilePath),
					getBytes(outputFilePath), 1);

			testNLPIR.NLPIR_NWI_Start();
			testNLPIR.NLPIR_NWI_AddFile(getBytes(inputFilePath));

			testNLPIR.NLPIR_NWI_Complete();

			nativeBytes = testNLPIR.NLPIR_NWI_GetResult(true);
			nativeStr = new String(nativeBytes, 0, nativeBytes.length, "UTF-8");

			System.out.println("�´�ʶ���� " + nativeStr);

			testNLPIR.NLPIR_NWI_Result2UserDict();// �´�ʶ����
			outputFilePath = "E:/NLPIR/test/test_result2.TXT";
			testNLPIR.NLPIR_FileProcess(getBytes(inputFilePath),
					getBytes(outputFilePath), 1);

			testNLPIR.NLPIR_Exit();
		} catch (Exception ex) {
		}
	}
}
