import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class SD_JD_TASK1 extends JFrame implements ActionListener {
    private JTextField display;
    private String operator = "";
    private double num1 = 0, num2 = 0;
    private boolean startNew = true;

    public SD_JD_TASK1() {
        setTitle("Advanced Java Calculator");
        setSize(400, 500);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout());

        // === Display Field ===
        display = new JTextField();
        display.setEditable(false);
        display.setFont(new Font("Arial", Font.BOLD, 28));
        add(display, BorderLayout.NORTH);

        // === Buttons Panel ===
        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(6, 4, 5, 5));

        // === Button Labels ===
        String[] buttons = {
            "C", "⌫", "%", "/",
            "√", "x²", "1/x", "*",
            "7", "8", "9", "-",
            "4", "5", "6", "+",
            "1", "2", "3", "=",
            "±", "0", ".", ""
        };

        for (String text : buttons) {
            if (!text.isEmpty()) {
                JButton btn = new JButton(text);
                btn.setFont(new Font("Arial", Font.BOLD, 20));
                btn.addActionListener(this);
                panel.add(btn);
            } else {
                panel.add(new JLabel()); // Empty slot
            }
        }

        add(panel, BorderLayout.CENTER);
    }

    public void actionPerformed(ActionEvent e) {
        String command = e.getActionCommand();

        if (command.matches("[0-9\\.]")) {
            if (startNew) {
                display.setText("");
                startNew = false;
            }
            display.setText(display.getText() + command);
        } else if (command.equals("C")) {
            display.setText("");
            num1 = num2 = 0;
            operator = "";
        } else if (command.equals("⌫")) {
            String current = display.getText();
            if (!current.isEmpty()) {
                display.setText(current.substring(0, current.length() - 1));
            }
        } else if (command.equals("±")) {
            try {
                double val = Double.parseDouble(display.getText());
                display.setText(String.valueOf(-val));
            } catch (Exception ex) {
                display.setText("Error");
            }
        } else if (command.equals("%")) {
            try {
                double val = Double.parseDouble(display.getText());
                display.setText(String.valueOf(val / 100));
            } catch (Exception ex) {
                display.setText("Error");
            }
        } else if (command.equals("√")) {
            try {
                double val = Double.parseDouble(display.getText());
                display.setText(String.valueOf(Math.sqrt(val)));
            } catch (Exception ex) {
                display.setText("Error");
            }
        } else if (command.equals("x²")) {
            try {
                double val = Double.parseDouble(display.getText());
                display.setText(String.valueOf(val * val));
            } catch (Exception ex) {
                display.setText("Error");
            }
        } else if (command.equals("1/x")) {
            try {
                double val = Double.parseDouble(display.getText());
                if (val == 0) {
                    display.setText("Cannot divide by 0");
                } else {
                    display.setText(String.valueOf(1 / val));
                }
            } catch (Exception ex) {
                display.setText("Error");
            }
        } else if (command.matches("[\\+\\-\\*/]")) {
            try {
                num1 = Double.parseDouble(display.getText());
                operator = command;
                startNew = true;
            } catch (Exception ex) {
                display.setText("Error");
            }
        } else if (command.equals("=")) {
            try {
                num2 = Double.parseDouble(display.getText());
                double result = 0;
                switch (operator) {
                    case "+": result = num1 + num2; break;
                    case "-": result = num1 - num2; break;
                    case "*": result = num1 * num2; break;
                    case "/":
                        if (num2 == 0) {
                            display.setText("Divide by 0 Error");
                            return;
                        }
                        result = num1 / num2;
                        break;
                }
                display.setText(String.valueOf(result));
                operator = "";
                startNew = true;
            } catch (Exception ex) {
                display.setText("Error");
            }
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
        	SD_JD_TASK1 calc = new SD_JD_TASK1();
            calc.setVisible(true);
        });
    }
}
