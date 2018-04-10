package first;

public class Hello_World {

	public static void main(String[] args) {
		System.out.println("Hello World!");
		/*
		java.util.Date date = new java.util.Date();
		java.sql.Date sqlDate = new java.sql.Date(date.getTime());
		java.sql.Timestamp timestamp = new java.sql.Timestamp(date.getTime());
		java.util.Date date2 = timestamp;
		
		System.out.println(date);
		System.out.println(sqlDate);
		System.out.println(timestamp);
		System.out.println(date2);
		*/
		java.util.Date date = null;
		java.sql.Timestamp timestamp = new java.sql.Timestamp(date.getTime());
		System.out.println(timestamp);
	}

}
