use std::f64::consts::{PI, E};

use errorfunctions::RealErrorFunctions;

fn f(x: f64) -> f64 {
    // let fval = (x - 1.0) / (x + 1.0);
    // let fval = (PI.sqrt() / 2.0) * RealErrorFunctions::erf(x);
    let fval = 1.0 / f64::tan(x);
    fval //return
}

fn df(x: f64) -> f64 {
    // let dfval = 2.0 / (x + 1.0).powf(2.0);
    // let dfval = E.powf(-x.powf(2.0));
    let dfval = -1.0/f64::sin(x).powf(2.0);
    
    dfval
}

fn dfapp_central(x: f64, h: f64) -> f64 {
    let appval = (f(x + h) - f(x - h)) / 2.0 * h;
    appval
}

fn dfapp_forward(x: f64, h: f64) -> f64 {
    let appval = (f(x + h) - f(x)) / h;
    appval
}

fn dfapp_backward(x: f64, h: f64) -> f64 {
    let appval = (f(x) - f(x - h)) / h;
    appval
}

fn error_value(actual: f64, approx: f64) -> f64 {
    
    (approx - actual).abs() //return
}

fn main() {
    
    let a_val = vec![1.570796];

    for a in a_val{
        let mut hval = 2.0;
        let df_exact = df(a);
        println!("a-value: {a}");
        for i in 0..10{
            let df_approx = dfapp_central(a, hval);
            let error = error_value(df_exact, df_approx);
            println!("exact: {df_exact}, approx.: {df_approx}, e: {error}, h: {hval}");
            hval = hval / 2.0 ;
        }
    }
    
}
