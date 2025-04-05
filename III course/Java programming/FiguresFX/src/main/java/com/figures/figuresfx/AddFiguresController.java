package com.figures.figuresfx;

import com.figures.exceptions.NullInputException;
import com.figures.figures.*;
import com.figures.figures.points.Point2D;
import com.figures.storage.Storage;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.Node;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.control.*;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

import java.util.Arrays;
import java.util.List;

public class AddFiguresController {

    private MainController mainController;
    private CrossFiguresController crossFiguresController;
    private MoveFiguresController moveFiguresController;
    private DeleteFiguresController deleteFiguresController;

    public void setControllers(MainController mainController, CrossFiguresController crossFiguresController, MoveFiguresController moveFiguresController, DeleteFiguresController deleteFiguresController) {
        this.mainController = mainController;
        this.crossFiguresController = crossFiguresController;
        this.moveFiguresController = moveFiguresController;
        this.deleteFiguresController = deleteFiguresController;
    }

    private FiguresApp application;

    public void setApplication(FiguresApp application) {
        this.application = application;
    }

    public AddFiguresController(){}

    @FXML
    private Spinner<Integer> numericUpDown1;

    @FXML
    private ComboBox<String> comboBox1;
    @FXML
    private Pane pn1;
    @FXML
    private Pane pn2;
    @FXML
    private Pane pn3;
    @FXML
    private Pane pn4;
    @FXML
    private Pane pn5;
    @FXML
    private Pane pn6;
    @FXML
    private Pane pn7;
    @FXML
    private Pane pn8;
    @FXML
    private Pane pn9;
    @FXML
    private Pane pn10;
    @FXML
    private Pane pn11;
    @FXML
    private Pane pn12;
    @FXML
    private Pane pn13;
    @FXML
    private Pane pn14;
    @FXML
    private Pane pn15;
    @FXML
    private Pane pn16;
    @FXML
    private Pane pn17;
    @FXML
    private Pane pn18;
    @FXML
    private TextField textBox1;
    @FXML
    private TextField textBox3;
    @FXML
    private TextField textBox2;
    @FXML
    private TextField textBox4;
    @FXML
    private TextField textBox5;
    @FXML
    private TextField textBox6;
    @FXML
    private TextField textBox7;
    @FXML
    private TextField textBox8;
    @FXML
    private TextField textBox9;
    @FXML
    private TextField textBox10;
    @FXML
    private TextField textBox11;
    @FXML
    private TextField textBox12;
    @FXML
    private TextField textBox13;
    @FXML
    private TextField textBox14;
    @FXML
    private TextField textBox15;
    @FXML
    private TextField textBox16;
    @FXML
    private TextField textBox17;
    @FXML
    private TextField textBox18;
    @FXML
    private TextField textBox19;
    @FXML
    private TextField textBox20;
    @FXML
    private TextField textBox21;
    @FXML
    private TextField textBox22;
    @FXML
    private TextField textBox23;
    @FXML
    private TextField textBox24;
    @FXML
    private TextField textBox25;
    @FXML
    private TextField textBox26;
    @FXML
    private TextField textBox27;
    @FXML
    private TextField textBox28;
    @FXML
    private TextField textBox29;
    @FXML
    private TextField textBox30;
    @FXML
    private TextField textBox31;
    @FXML
    private TextField textBox32;
    @FXML
    private TextField textBox33;
    @FXML
    private TextField textBox34;
    @FXML
    private TextField textBox35;
    @FXML
    private TextField textBox36;
    @FXML
    private TextField textBox37;
    @FXML
    private Label label1;

    public void initialize(){
        // Создание SpinnerValueFactory и настройка минимального и максимального значения
        SpinnerValueFactory<Integer> valueFactory = new SpinnerValueFactory.IntegerSpinnerValueFactory(1, 100, 1);

        // Установка SpinnerValueFactory для Spinner
        numericUpDown1.setValueFactory(valueFactory);
        comboBox1.getItems().addAll("Отрезок",
                "Ломанная",
                "Окружность",
                "Многоугольник",
                "Треугольник",
                "Четырёхугольник",
                "Прямоугольник",
                "Трапеция");
        SpinnerValueFactory<Integer> valueFactory_nup = new SpinnerValueFactory.IntegerSpinnerValueFactory(
                1, // Минимальное значение
                18, // Максимальное значение
                1 // Начальное значение
        );
        numericUpDown1.setValueFactory(valueFactory_nup);
        // Устанавливаем слушатель событий на изменение значения Spinner
        numericUpDown1.valueProperty().addListener(new ChangeListener<Integer>() {
            @Override
            public void changed(ObservableValue<? extends Integer> observable, Integer oldValue, Integer newValue) {
                // В этом методе обрабатываем изменение значения Spinner
                int value = numericUpDown1.getValue();
                List<Pane> panes = Arrays.asList(pn1, pn2, pn3, pn4, pn5, pn6, pn7, pn8, pn9, pn10, pn11, pn12, pn13, pn14, pn15, pn16, pn17, pn18);

                for (int i = 0; i < 18; i++) {
                    panes.get(i).setVisible(i < value);
                }

                Storage.pointsCount = value;
            }
        });
    }
    @FXML
    public void comboBox1_SelectedIndexChanged(ActionEvent actionEvent) {
        numericUpDown1.setVisible(true);
        pn1.setVisible(true);

        String selectedValue = comboBox1.getValue();

        label1.setVisible(false);
        textBox1.setVisible(false);
        numericUpDown1.setDisable(false);

        switch (selectedValue) {
            case "Отрезок":
                numericUpDown1.getValueFactory().setValue(2);
                numericUpDown1.setDisable(true);
                break;
            case "Ломанная":
                break;
            case "Треугольник":
                numericUpDown1.getValueFactory().setValue(3);
                numericUpDown1.setDisable(true);
                break;
            case "Окружность":
                label1.setVisible(true);
                textBox1.setVisible(true);
                numericUpDown1.getValueFactory().setValue(1);
                numericUpDown1.setDisable(true);
                break;
            case "Многоугольник":
                label1.setVisible(false);
                textBox1.setVisible(false);
                break;
            case "Трапеция", "Четырёхугольник", "Прямоугольник":
                numericUpDown1.getValueFactory().setValue(4);
                label1.setVisible(false);
                textBox1.setVisible(false);
                numericUpDown1.setDisable(true);
                break;
        }
    }

    @FXML
    private void button4_Click(ActionEvent event) {
        try {
            if (comboBox1.getSelectionModel().getSelectedIndex() == -1) {
                throw new NullInputException();
            }
            update();
            Storage.getListPoints().clear();
            switch (Storage.getPointsCount()) {
                case 1:
                    Storage.getListPoints().add(Double.parseDouble(textBox3.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox2.getText()));
                    break;
                case 2:
                    Storage.getListPoints().add(Double.parseDouble(textBox3.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox2.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox8.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox9.getText()));
                    break;
                case 3:
                    Storage.getListPoints().add(Double.parseDouble(textBox3.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox2.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox8.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox9.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox10.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox11.getText()));
                    break;
                case 4:
                    Storage.getListPoints().add(Double.parseDouble(textBox3.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox2.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox8.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox9.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox10.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox11.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox12.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox13.getText()));
                    break;
                case 5:
                    Storage.getListPoints().add(Double.parseDouble(textBox3.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox2.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox8.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox9.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox10.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox11.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox12.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox13.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox14.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox15.getText()));
                    break;
                case 6:
                    Storage.getListPoints().add(Double.parseDouble(textBox3.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox2.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox8.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox9.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox10.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox11.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox12.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox13.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox14.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox15.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox16.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox17.getText()));
                    break;
                case 7:
                    Storage.getListPoints().add(Double.parseDouble(textBox3.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox2.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox8.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox9.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox10.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox11.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox12.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox13.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox14.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox15.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox16.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox17.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox4.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox5.getText()));
                    break;
                case 8:
                    Storage.getListPoints().add(Double.parseDouble(textBox3.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox2.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox8.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox9.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox10.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox11.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox12.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox13.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox14.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox15.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox16.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox17.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox4.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox5.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox18.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox19.getText()));
                    break;
                case 9:
                    Storage.getListPoints().add(Double.parseDouble(textBox3.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox2.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox8.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox9.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox10.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox11.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox12.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox13.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox14.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox15.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox16.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox17.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox4.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox5.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox18.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox19.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox20.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox21.getText()));
                    break;
                case 10:
                    Storage.getListPoints().add(Double.parseDouble(textBox3.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox2.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox8.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox9.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox10.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox11.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox12.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox13.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox14.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox15.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox16.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox17.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox4.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox5.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox18.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox19.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox20.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox21.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox22.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox23.getText()));
                    break;
                case 11:
                    Storage.getListPoints().add(Double.parseDouble(textBox3.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox2.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox8.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox9.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox10.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox11.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox12.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox13.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox14.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox15.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox16.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox17.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox4.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox5.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox18.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox19.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox20.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox21.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox24.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox25.getText()));
                    break;
                case 12:
                    Storage.getListPoints().add(Double.parseDouble(textBox3.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox2.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox8.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox9.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox10.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox11.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox12.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox13.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox14.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox15.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox16.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox17.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox4.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox5.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox18.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox19.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox20.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox21.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox24.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox25.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox26.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox27.getText()));
                    break;
                case 13:
                    Storage.getListPoints().add(Double.parseDouble(textBox3.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox2.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox8.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox9.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox10.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox11.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox12.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox13.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox14.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox15.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox16.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox17.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox4.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox5.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox18.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox19.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox20.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox21.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox24.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox25.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox26.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox27.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox6.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox7.getText()));
                    break;
                case 14:
                    Storage.getListPoints().add(Double.parseDouble(textBox3.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox2.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox8.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox9.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox10.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox11.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox12.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox13.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox14.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox15.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox16.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox17.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox4.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox5.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox18.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox19.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox20.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox21.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox24.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox25.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox26.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox27.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox6.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox7.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox28.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox29.getText()));
                    break;
                case 15:
                    Storage.getListPoints().add(Double.parseDouble(textBox3.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox2.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox8.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox9.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox10.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox11.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox12.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox13.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox14.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox15.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox16.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox17.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox4.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox5.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox18.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox19.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox20.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox21.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox24.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox25.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox26.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox27.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox6.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox7.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox28.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox29.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox30.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox31.getText()));
                    break;
                case 16:
                    Storage.getListPoints().add(Double.parseDouble(textBox3.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox2.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox8.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox9.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox10.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox11.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox12.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox13.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox14.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox15.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox16.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox17.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox4.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox5.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox18.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox19.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox20.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox21.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox24.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox25.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox26.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox27.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox6.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox7.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox28.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox29.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox30.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox31.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox32.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox33.getText()));
                    break;
                case 17:
                    Storage.getListPoints().add(Double.parseDouble(textBox3.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox2.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox8.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox9.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox10.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox11.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox12.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox13.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox14.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox15.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox16.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox17.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox4.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox5.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox18.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox19.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox20.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox21.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox24.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox25.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox26.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox27.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox6.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox7.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox28.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox29.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox30.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox31.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox32.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox33.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox34.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox35.getText()));
                case 18:
                    Storage.getListPoints().add(Double.parseDouble(textBox3.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox2.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox8.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox9.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox10.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox11.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox12.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox13.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox14.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox15.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox16.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox17.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox4.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox5.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox18.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox19.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox20.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox21.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox24.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox25.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox26.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox27.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox6.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox7.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox28.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox29.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox30.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox31.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox32.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox33.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox34.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox35.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox36.getText()));
                    Storage.getListPoints().add(Double.parseDouble(textBox37.getText()));
                    break;
            }

            String figure = comboBox1.getValue();
            switch (figure) {
                case "Окружность":
                    Storage.getListFigures().add(new Circle(new Point2D(new double[]{Double.parseDouble(Storage.getListPoints().get(0).toString()), Double.parseDouble(Storage.getListPoints().get(1).toString())}), Double.parseDouble(textBox1.getText())));
                    Storage.nameFigures.add("Окружность");
                    Storage.figuresCount++;
                    break;
                case "Отрезок":
                    Storage.getListFigures().add(new Segment(new Point2D(new double[]{Double.parseDouble(Storage.getListPoints().get(0).toString()), Double.parseDouble(Storage.getListPoints().get(1).toString())}),
                            new Point2D(new double[]{Double.parseDouble(Storage.getListPoints().get(2).toString()),
                                    Double.parseDouble(Storage.getListPoints().get(3).toString())})));
                    Storage.nameFigures.add("Отрезок");
                    Storage.figuresCount++;
                    break;
                case "Ломанная": // Если фигура - полилиния
                case "Многоугольник": // Если фигура - правильный n-угольник
                case "Четырёхугольник": // Если фигура - квадрат
                case "Треугольник": // Если фигура - равнобедренный треугольник
                case "Трапеция": // Если фигура - трапеция
                case "Прямоугольник": // Если фигура - прямоугольник
                    int k = Integer.parseInt(numericUpDown1.getValue().toString());
                    Point2D[] coords = new Point2D[k];
                    for (int i = 0, j = 0; i < k; i++, j += 2) {
                        coords[i] = new Point2D(new double[]{Storage.getListPoints().get(j), Storage.getListPoints().get(j + 1)});
                    }
                    // Добавление фигуры в список в зависимости от типа
                    if (figure == "Ломанная") {
                        Storage.getListFigures().add(new Polyline(coords));
                        Storage.nameFigures.add("Ломанная");
                        Storage.figuresCount++;
                    }
                    if (figure == "Многоугольник") {
                        Storage.getListFigures().add(new NGon(coords));
                        Storage.nameFigures.add("Многоугольник");
                        Storage.figuresCount++;
                    }
                    if (figure == "Четырёхугольник") {
                        Storage.getListFigures().add(new QGon(coords));
                        Storage.nameFigures.add("Четырёхугольник");
                        Storage.figuresCount++;
                    }
                    if (figure == "Треугольник") {
                        Storage.getListFigures().add(new TGon(coords));
                        Storage.nameFigures.add("Треугольник");
                        Storage.figuresCount++;
                    }
                    if (figure == "Трапеция") {
                        Storage.getListFigures().add(new Trapeze(coords));
                        Storage.nameFigures.add("Трапеция");
                        Storage.figuresCount++;
                    }
                    if (figure == "Прямоугольник") {
                        Storage.getListFigures().add(new Rectangle(coords));
                        Storage.nameFigures.add("Прямоугольник");
                        Storage.figuresCount++;
                    }
                    break;
            }
            Canvas canvas = mainController.canvas;
            GraphicsContext gc = mainController.canvas.getGraphicsContext2D();
            gc.clearRect(0, 0, canvas.getWidth(), canvas.getHeight());
            application.drawAxes(canvas.getWidth(), canvas.getHeight());
            for(int i = 0; i < Storage.figuresCount; i++){
                mainController.draw(Storage.getListFigures().get(i), Color.BLACK);
            }
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setTitle("Успех");
            alert.setHeaderText(null);
            alert.setContentText("Добавление завершено");
            alert.showAndWait();
        } catch (NullInputException ex) {
            Alert alert = new Alert(Alert.AlertType.WARNING);
            alert.setTitle("Ошибка");
            alert.setHeaderText(null);
            alert.setContentText(ex.toString());
            alert.showAndWait();
        } catch (NumberFormatException ex) {
            Alert alert = new Alert(Alert.AlertType.WARNING);
            alert.setTitle("Ошибка");
            alert.setHeaderText(null);
            alert.setContentText("Выбраны не все значения!");
            alert.showAndWait();

        } catch (IllegalArgumentException ex) {
            Alert alert = new Alert(Alert.AlertType.WARNING);
            alert.setTitle("Ошибка");
            alert.setHeaderText(null);
            alert.setContentText(ex.getMessage());
            alert.showAndWait();
        }
    }

    public void update() {
        Storage.setPointsCount(numericUpDown1.getValue());
    }

    public void buttonCancel_Click(ActionEvent actionEvent) {
        Stage stage = (Stage) ((Node) actionEvent.getSource()).getScene().getWindow();

        // Закрыть текущую сцену (форму)
        stage.close();
    }
}
