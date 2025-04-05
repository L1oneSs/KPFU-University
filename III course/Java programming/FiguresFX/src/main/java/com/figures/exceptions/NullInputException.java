package com.figures.exceptions;

public class NullInputException extends Exception {
    public NullInputException() { }

    @Override
    public String toString() {
        return "Выбраны не все значения!";
    }
}
