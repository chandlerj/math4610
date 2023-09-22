

fn maceps_float_f32() -> f32{
    let one:f32 = 1.0;
    let mut h:f32 = 1.0;
    let mut appone = one + h;
    let mut error = (appone - one).abs();
    
    while error > 0.0 {
        h = h / 2.0;
        appone = one + h;
        error = (appone - one).abs();
        
    }

    h
}

fn maceps_float_f64() -> f64{
    let one:f64 = 1.0;
    let mut h:f64 = 1.0;
    let mut appone = one + h;
    let mut error = (appone - one).abs();
    
    while error > 0.0 {
        h = h / 2.0;
        appone = one + h;
        error = (appone - one).abs();
        
    }

    h
}

fn two_norm(v: &[f64]) -> f64{
    let mut sum: f64 = 0.0;
    
    for i in 0..v.len(){
        sum += v[i] * v[i];
    }

    sum = sum.sqrt();
    sum
}

fn one_norm(v: &[f64]) -> f64{
    let mut sum: f64 = 0.0;
    
    for i in 0..v.len(){
        sum += v[i].abs();
    }

    sum
}

fn inf_norm(v: &[f64]) -> f64 {
    let mut max = 0.0;
    
    for i in 0..v.len(){
        let abs: f64 = v[i].abs();
        if abs > max{
            max = abs;
        }
    }
    
    max
}

fn two_norm_dist(v1: &[f64], v2: &[f64]) -> f64 {
    if v1.len() != v2.len(){
        panic!("cannot compute two norm as vectors are different sizes.");
    }
    let mut sum: f64 = 0.0;
    for i in 0..v1.len(){
        let distance = v1[i] - v2[i];
        sum += distance * distance;
    }
    sum = sum.sqrt();
    
    //return
    sum
}

fn one_norm_dist(v1: &[f64], v2: &[f64]) -> f64 {
    if v1.len() != v2.len(){
        panic!("cannot compute two norm as vectors are different sizes.");
    }
    let mut sum: f64 = 0.0;
    for i in 0..v1.len() {
        let distance = v1[i] - v2[i];
        sum += distance.abs();
    }
    //return
    sum
}

fn inf_norm_dist(v1: &[f64], v2: &[f64]) -> f64 {
    if v1.len() != v2.len(){
        panic!("cannot compute two norm as vectors are different sizes.");
    }
    let mut max: f64 = 0.0;
    for i in 0..v1.len(){
        let distance = (v1[i] - v2[i]).abs();
        if distance > max {
            max = distance;
        }
    }

    max
}

fn main() {
    let maceps_f32 = maceps_float_f32();
    let maceps_f64 = maceps_float_f64();
    let vector:&[f64] = &[2.4,4.0,3.14,2.0];
    let vector2:&[f64] = &[4.0,6.7,4.9,-4.5];
    let v2_norm = two_norm(vector);
    let v1_norm = one_norm(vector2);
    let infinity_norm = inf_norm(vector2);
    let v2_norm_dist = two_norm_dist(vector, vector2);
    let v1_norm_dist = one_norm_dist(vector, vector2);
    let inf_norm_dist = inf_norm_dist(vector, vector2);
    // println!("Maceps float to 32-bits of precision: {maceps_f32}");
    // println!("Maceps float to 64-bits of precision: {maceps_f64}");
    // println!("two norm of {vector:?}: {v2_norm}");
    // println!("one norm of {vector2:?}: {v1_norm}");
    // println!("infinity norm of {vector2:?}: {infinity_norm}");
    println!("two norm of {vector:?} & {vector2:?}: {v2_norm_dist}");
    println!("one norm of {vector:?} & {vector2:?}: {v1_norm_dist}");
    println!("inf norm of {vector:?} & {vector2:?}: {inf_norm_dist}");
}
