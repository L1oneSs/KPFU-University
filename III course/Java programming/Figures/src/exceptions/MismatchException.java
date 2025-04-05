package exceptions;

public class MismatchException extends Exception {
    public MismatchException() { }

    @Override
    public String toString() {
        return "Выберите соответствующие параметры для ввода!";
    }
}
