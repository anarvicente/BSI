import java.awt.*;

public class Figura {
	private int x, y;
	String id;

	public Figura(String id,int px, int py) {
		x = px;
		y = py;
		this.id = id;
	}
	public void imp() {
		System.out.println( "Id: "+ getId() + "\nCentro(" + getX() + ", " + getY() +")" );
	}

	public int getX() {
		return x;
	}

	public int getY() {
		return y;
	}

	public void setX(int x){
		this.x = x;
	}

	public void setY(int y){
		this.y = y;
	}
	
	public String getId(){
		return id;
	}

	public void desenhe(Graphics2D g2d){ }
	
	public  static void mostraFiguras(PilhaFigura p){
		PilhaFigura aux = new PilhaFigura();
		Figura n;
		aux.crie();

		while(!p.vazia()){
			n = (Figura)p.desempilhe();
			n.imp();
			aux.empilhe(n);
		}
	}
}
