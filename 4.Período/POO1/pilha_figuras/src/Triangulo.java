import java.awt.*;

public class Triangulo extends Figura {
	
	private int lado;
	
	public Triangulo(String id,int lado, int x, int y){
		super(id,x,y);
		this.lado = lado;
	}

	public void desenhe(Graphics2D g2d){
		Polygon poligono = new Polygon();
		poligono.addPoint(getX(),getY());
		poligono.addPoint(getX() + (getLado()/2),getY() + getLado());
		poligono.addPoint(getX() - (getLado()/2),getY() + getLado());
		g2d.drawPolygon(poligono);

	}

	public void imp(){
		super.imp();
		System.out.println("Lado = " + this.lado);
	}

	public void setLado(int lado){
		this.lado = lado;
	}
	
	public int getLado(){
		return this.lado;
	}


	
}
