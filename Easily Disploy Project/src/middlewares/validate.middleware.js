
// Hoisted declaration = function
// or class 
// assignment expression

import { body, validationResult } from "express-validator";

  
const validateRequest = async (req, res, next) =>{
    // const { name, price, imageUrl } = req.body;
    // let errors = [];
    // if (!name || name.trim() == '') {
    //   errors.push('Name is required');
    // }
    // if (!price || parseFloat(price) < 1) {
    //   errors.push(
    //     'Price must be a positive value'
    //   );
    // }
    // try {
    //   const validUrl = new URL(imageUrl);
    // } catch (err) {
    //   errors.push('URL is invalid');
    // }
    
    console.log(req.body);

    //1. Setup Rupes for Validation
    const rules = [
        body('jobCategory')
          .notEmpty()
          .withMessage('Job Category Mandatory'),
        body('jobDesignation')
            .notEmpty()
            .withMessage('Job Designation Mandatory'),
        body('jobLocation')
            .notEmpty()
            .withMessage('Job Location Mandatory'),
        body('companyname')
            .notEmpty()
            .withMessage('Job companyname Mandatory'),
        body('salary')
        .notEmpty()
        .withMessage('Job companyname Mandatory'),
        body('numberofopenings')
          .isFloat({ gt: 0 })
          .withMessage(
            'Price should be a positive value'
          ),
        body('skillsrequired')
          .notEmpty()
          .withMessage('Job skillsrequired Mandatory'),
        body('applyby')
        .notEmpty()
        .withMessage('Job skillsrequired Mandatory'),
        
      ];

    //2. run those rules
    await Promise.all(
        rules.map((rule) => rule.run(req))
      );
    //3. check if is there any error after running the rules
    var validationErrors = validationResult(req);
  console.log(validationErrors);
 // 4. if errros, return the error message
 if (!validationErrors.isEmpty()) {
    return res.render('postNewJob', {
      errorMessage:
      validationErrors.array()[0].msg,
      userEmail: req.session.userEmail
    });
  }
  next();

}

export default validateRequest;