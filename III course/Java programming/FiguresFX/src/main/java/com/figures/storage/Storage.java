package com.figures.storage;

import com.figures.interfaces.IShape;

import java.util.ArrayList;
import java.util.List;

public class Storage {

    public static int figuresCount = 0;
    public static int pointsCount = 0;
    public static List<IShape> listFigures = new ArrayList<>();
    public static List<Double> listPoints = new ArrayList<>();

    public static List<String> nameFigures = new ArrayList<>();

    public static void setPointsCount(int value) {
        pointsCount = value;
    }


    public void setFiguresCount(int value) {
        figuresCount = value;
    }

    public void incPointsCount(){
        pointsCount++;
    }

    public static void incFiguresCount(){
        figuresCount++;
    }

    public static void decFiguresCount(){
        figuresCount--;
    }

    public static int getPointsCount() {
        return pointsCount;
    }

    public static int getFiguresCount() {
        return figuresCount;
    }


    public static List<Double> getListPoints(){
        return listPoints;
    }

    public static List<IShape> getListFigures(){
        return listFigures;
    }

}
