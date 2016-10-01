
public class PilhaFigura {
	 private static final int Max = 100;
	 private int topo;
	 private int NFiguras;
	 private Object []vet;
	 
	 public void crie() {
		 topo = -1;
		 vet = new Object[Max];
	 }
	 
	 public boolean empilhe(Object elem) {
		 if ( topo >= Max - 1) return false;
		 else {++topo;
		 vet[topo] = elem;
		 NFiguras++;
		 return true;
		 }
	}
	public Object desempilhe() {
		Object elem = new Object();
		if ( topo < 0 ) return null;
		else {
			elem = vet[topo];
			topo = topo - 1;
			return elem;
		}
	}
	
	public boolean vazia() {
	return topo < 0;
	}
	
	public int getNFiguras(){
		return NFiguras;
	}
	
}