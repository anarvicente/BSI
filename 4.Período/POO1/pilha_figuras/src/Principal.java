

public class Principal {
	
	public static void main(String [] args){
		PilhaFigura p = new PilhaFigura();
		p.crie();
		Object n;
		Circulo c1 = new Circulo("c1",100,400,300);
		Circulo c2 = new Circulo("c2",200,400,300);
		Quadrado q1 = new Quadrado("q1",200,400,300);
		Quadrado q2 = new Quadrado("q2",100,400,300);
		Triangulo t1 = new Triangulo("t1",30,400,300);
		Triangulo t2 = new Triangulo("t2",100,430,300);
		
		p.empilhe(c1);
		p.empilhe(q1);
		p.empilhe(c2);
		p.empilhe(q2);
		p.empilhe(t1);
		p.empilhe(t2);
		
		new Example01(p);
		
	}

}
