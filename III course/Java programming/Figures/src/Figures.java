import figures.*;
import figures.points.Point2D;
import interfaces.IShape;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class Figures {
    private int k = 0;
    private int figures_count = 0;
    private List<IShape> list = new ArrayList<>();
    private List<IShape> list1 = new ArrayList<>();
    private List<IShape> list2 = new ArrayList<>();

    public Figures() {
        // Настройка локали
        Locale.setDefault(Locale.US);
        Figures();
    }

    public void Figures() {
        k = 0;
        figures_count = 0;

        try {
            BufferedReader reader = new BufferedReader(new FileReader("files/file.txt"));
            String n = reader.readLine();
            figures_count = Integer.parseInt(n);

            String line;

            while ((line = reader.readLine()) != null) {
                String[] values = line.split(" ");
                String figure = values[0];

                switch (figure) {
                    case "Circle":
                        list.add(new Circle(new Point2D(new double[]{Double.parseDouble(values[1]), Double.parseDouble(values[2])}), Double.parseDouble(values[3])));
                        break;
                    case "Segment":
                        list.add(new Segment(new Point2D(new double[]{Double.parseDouble(values[1]), Double.parseDouble(values[2])}),
                                new Point2D(new double[]{Double.parseDouble(values[3]), Double.parseDouble(values[4])})));
                        break;
                    case "Polyline":
                    case "NGon":
                    case "QGon":
                    case "TGon":
                    case "Trapeze":
                    case "Rectangle":
                        int k = Integer.parseInt(values[1]);
                        Point2D[] pr = new Point2D[k];
                        for (int i = 0, j = 2; i < k; i++, j += 2) {
                            pr[i] = new Point2D(new double[]{Double.parseDouble(values[j]), Double.parseDouble(values[j + 1])});
                        }
                        if (figure.equals("Polyline")) list.add(new Polyline(pr));
                        if (figure.equals("NGon")) list.add(new NGon(pr));
                        if (figure.equals("QGon")) list.add(new QGon(pr));
                        if (figure.equals("TGon")) list.add(new TGon(pr));
                        if (figure.equals("Trapeze")) list.add(new Trapeze(pr));
                        if (figure.equals("Rectangle")) list.add(new Rectangle(pr));
                        break;
                    default:
                        System.out.println("Введён неверный тип фигуры: " + figure);
                        break;
                }
            }
            reader.close();
        } catch (IOException ex) {
            System.out.println("Ошибка чтения файла: " + ex.getMessage());
        }

        double sum_square = 0;
        double sum_length = 0;

        for (var v : list) {
            //String typeName = v.getClass().getSimpleName();
            //System.out.print(typeName + ": ");
            //System.out.print(v.toString());
            //System.out.print("Длина: " + Math.round(v.length() * 100.0) / 100.0);
            sum_length += v.length();
            //System.out.print("Площадь: " + Math.round(v.square() * 100.0) / 100.0);
            sum_square += v.square();
        }

        System.out.println("Суммарная площадь: " + Math.round(sum_square * 100.0) / 100.0);
        System.out.println("Суммарная длина: " + Math.round(sum_length * 100.0) / 100.0);
        System.out.println("Средняя площадь: " + Math.round((sum_square / figures_count) * 100.0) / 100.0);
        System.out.println();

        try {
            BufferedReader reader = new BufferedReader(new FileReader("files/file1.txt"));
            String line;

            int q = 0;
            while ((line = reader.readLine()) != null) {
                String[] values = line.split(" ");

                String figure = list.get(q).getClass().getSimpleName();

                switch (figure) {
                    case "Circle":
                        list1.add(new Circle(new Point2D(new double[]{Double.parseDouble(values[0]), Double.parseDouble(values[1])}),
                                Double.parseDouble(values[2])));
                        break;
                    case "Segment":
                        list1.add(new Segment(new Point2D(new double[]{Double.parseDouble(values[0]), Double.parseDouble(values[1])}),
                                new Point2D(new double[]{Double.parseDouble(values[2]), Double.parseDouble(values[3])})));
                        break;
                    case "Polyline":
                    case "NGon":
                    case "QGon":
                    case "TGon":
                    case "Trapeze":
                    case "Rectangle":
                        int k = Integer.parseInt(values[0]);
                        Point2D[] pr = new Point2D[k];
                        for (int i = 0, j = 1; i < k; i++, j += 2) {
                            pr[i] = new Point2D(new double[]{Double.parseDouble(values[j]), Double.parseDouble(values[j + 1])});
                        }
                        if (figure.equals("Polyline")) list1.add(new Polyline(pr));
                        if (figure.equals("NGon")) list1.add(new NGon(pr));
                        if (figure.equals("QGon")) list1.add(new QGon(pr));
                        if (figure.equals("TGon")) list1.add(new TGon(pr));
                        if (figure.equals("Trapeze")) list1.add(new Trapeze(pr));
                        if (figure.equals("Rectangle")) list1.add(new Rectangle(pr));
                        break;
                    default:
                        System.out.println("Введён неверный тип фигуры: " + figure);
                        break;
                }
                q++;
            }
            reader.close();
        } catch (IOException ex) {
            System.out.println("Ошибка чтения файла: " + ex.getMessage());
        }

        for (int i = 0; i < figures_count; i++) {
            String typeName = list.get(i).getClass().getSimpleName();
            System.out.print("Пересекаются ли " + typeName + ": ");
            if (list.get(i).cross(list1.get(i))) {
                System.out.println("да");
            } else {
                System.out.println("нет");
            }
        }

        try {
            BufferedReader reader = new BufferedReader(new FileReader("files/file2.txt"));
            String line;
            int w = 0;

            while ((line = reader.readLine()) != null) {
                String[] values = line.split(" ");

                String move = values[0];

                switch (move) {
                    case "rot":
                        list2.add(list1.get(w).rot(Double.parseDouble(values[1])));
                        break;
                    case "symAxis":
                        list2.add(list1.get(w).symAxis(Integer.parseInt(values[1])));
                        break;
                    case "shift":
                        list2.add(list1.get(w).shift(new Point2D(new double[]{Double.parseDouble(values[1]), Double.parseDouble(values[2])})));
                        break;
                    default:
                        System.out.println("Введён неверный тип фигуры: " + move);
                        break;
                }
                w++;
            }
            reader.close();
        } catch (IOException ex) {
            System.out.println("Ошибка чтения файла: " + ex.getMessage());
        }

        System.out.println();
        System.out.print("После движения фигур: ");
        System.out.println();
        for (int i = 0; i < figures_count; i++) {
            String typeName = list.get(i).getClass().getSimpleName();
            System.out.print("Пересекаются ли " + typeName + ": ");
            if (list.get(i).cross(list2.get(i))) {
                System.out.println("да");
            } else {
                System.out.println("нет");
            }
        }
    }


}