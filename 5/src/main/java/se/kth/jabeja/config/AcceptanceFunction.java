package se.kth.jabeja.config;

/**
 *
 */
public enum AcceptanceFunction {
    SIMPLE("SIMPLE"),
    EXPONENTIAL("EXPONENTIAL");
    String name;
    AcceptanceFunction(String name) {
        this.name = name;
    }
    @Override
    public String toString() {
        return name;
    }
}
