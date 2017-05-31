class Sleeping {
	public static void main(String[] args) {
		String x = "Hello, World!";
		for (int i = 0; i<x.length(); i++) {
			System.out.print(x.charAt(i));
			try {                   //ÝÒÀ ×ÀÑÒÜ ÊÎÄÀ ÂÛÇÛÂÀÅÒ ÑÏßÙÓÞ ÎØÈÁÊÓ, ÊÎÒÎÐÀß ÌÎÆÅÒ
				Thread.sleep(150);  //ÁÛÒÜ ÍÓÆÍÀ ÄËß ÏÎÄÐÎÁÍÎÃÎ ÎÑÌÎÒÐÀ ÊÎÄÀ ÈËÈ
			}catch (Exception e) {} //ÌÎÆÅÒ ÑÎÇÄÀÒÜ ÐÀÇËÈ×ÍÛÅ ÝÔÔÅÊÒÛ (ÏÅ×ÀÒÍÀß ÌÀØÈÍÊÀ).
		}                           
	}
}