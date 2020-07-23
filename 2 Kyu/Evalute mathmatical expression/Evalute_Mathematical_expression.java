import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;

public class MathEvaluator {

    public double calculate(String exp) {
        double x = 0;
        System.out.println("exp : " + exp);
        ScriptEngineManager scriptEngineManager = new ScriptEngineManager();
        ScriptEngine Engine = scriptEngineManager.getEngineByName("JavaScript");
        try {
            String ss = Engine.eval(exp).toString();
            x = Double.parseDouble(ss);
        } catch (ScriptException e1) {
            e1.printStackTrace();
        }
        return x;
    }

}